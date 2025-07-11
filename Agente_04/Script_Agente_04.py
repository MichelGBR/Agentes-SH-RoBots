import re
import time
import os
import requests
import pdfplumber
from io import BytesIO
from playwright.sync_api import Playwright, sync_playwright
import pandas as pd

def run(playwright: Playwright) -> None:
    base_comb = pd.read_excel("base_dados.xlsx", engine='openpyxl')

    if "cpf" not in base_comb.columns:
        base_comb["cpf"] = ""
    if "vigencia" not in base_comb.columns:
        base_comb["vigencia"] = ""

    usuario = os.getenv("APP_USUARIO")
    senha = os.getenv("APP_SENHA")

    if not usuario or not senha:
        raise ValueError("Credenciais não encontradas. Configure as variáveis de ambiente APP_USUARIO e APP_SENHA.")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # URL genérica
    page.goto("https://www.sistemagenerico.com/login")
    time.sleep(2)
    page.get_by_role("textbox", name="Usuário").fill(usuario)
    page.get_by_role("textbox", name="Senha").fill(senha)
    page.get_by_role("textbox", name="Senha").press("Enter")
    time.sleep(2)

    for index, row in base_comb.iterrows():
        numero = str(int(row["número"]))
        print(f"\n🔍 Pesquisando número: {numero}")

        try:
            time.sleep(1)
            page.locator("li:nth-child(2) > a").first.click()
            page.get_by_role("link", name="Consulta de Dados").click()
            time.sleep(2)

            page.get_by_role("textbox", name="Pesquisar").click()
            page.get_by_role("textbox", name="Pesquisar").fill(numero)
            page.get_by_role("button", name="Pesquisar").click()
            time.sleep(2)

            page.get_by_role("cell", name="Resultado").locator("a").click()
            time.sleep(3)
            page.locator('a[onclick*="abrirPDF"]').click()
            time.sleep(1)

            for tentativa in range(2):
                try:
                    page.locator("label[for='SelecionarPDF']").click()
                    with page.expect_popup() as page1_info:
                        time.sleep(1)
                        page.get_by_role("row", name="Documento").locator('img[src*="pdf-icon.png"]').click()
                        time.sleep(1)
                        page.get_by_role("row", name="Documento").locator('img[src*="pdf-icon.png"]').click()

                    page1 = page1_info.value
                    time.sleep(1)
                    page1.close()
                    break
                except Exception as e:
                    print(f"⚠️ Tentativa {tentativa + 1} falhou: {e}")
                    time.sleep(1)
            else:
                print("❌ Não foi possível abrir o PDF após 2 tentativas.")
                continue

            pdf_url = page1.url
            response = requests.get(pdf_url)

            if response.status_code == 200:
                with pdfplumber.open(BytesIO(response.content)) as pdf:
                    text = ""
                    for p in pdf.pages:
                        page_text = p.extract_text()
                        if page_text:
                            text += page_text + "\n"

                    cpf_match = re.search(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b", text)
                    cpf_extraido = re.sub(r"[.-]", "", cpf_match.group()) if cpf_match else "Não encontrado"

                    vigencia_match = re.search(r"Vigência:\s*(\d{2}/\d{2}/(\d{4}))\s*a\s*(\d{2}/\d{2}/(\d{4}))", text)
                    if vigencia_match:
                        ano_inicio = int(vigencia_match.group(2))
                        ano_fim = int(vigencia_match.group(4))
                        vigencia_extraida = str(ano_fim - ano_inicio)
                    else:
                        vigencia_extraida = "Não encontrada"

                    base_comb.at[index, "cpf"] = cpf_extraido
                    base_comb.at[index, "vigencia"] = vigencia_extraida
            else:
                print("❌ Erro ao baixar o PDF:", response.status_code)

        except Exception:
            continue

    base_comb.to_excel("base_dados_atualizada.xlsx", index=False)
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
