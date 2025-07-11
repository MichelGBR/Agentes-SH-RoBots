import time
import os
from playwright.sync_api import Playwright, sync_playwright
from colorama import Fore, Style

def run(playwright: Playwright) -> None:
    # Carrega credenciais de variáveis de ambiente
    usuario = os.getenv("APP_USUARIO")
    senha = os.getenv("APP_SENHA")

    if not usuario or not senha:
        raise ValueError("Credenciais não encontradas. Configure as variáveis de ambiente APP_USUARIO e APP_SENHA.")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # URL genérica
    page.goto("https://www.sistemagenerico.com/login")
    time.sleep(1)

    # Login
    page.get_by_role("textbox", name="Usuário").fill(usuario)
    page.get_by_role("textbox", name="Senha").fill(senha)
    page.get_by_role("button", name="Entrar").click()
    time.sleep(1)

    # Seleção de parceiro genérica
    page.locator("#selecao-parceiro").get_by_text("Selecionar").click()
    page.locator("#opcao-parceiro").get_by_text("Parceiro X").click()
    time.sleep(1)

    # Navegação genérica
    page.get_by_role("button").filter(has_text="Menu").click()
    page.get_by_text("Relatórios").click()
    page.get_by_text("Sinistros").click()
    time.sleep(1)

    # Seleção de datas genérica
    page.locator("mat-form-field").filter(has_text="De").get_by_label("Abrir calendário").click()
    page.get_by_role("button", name="Mês anterior").click()
    page.get_by_role("button", name="Mês anterior").click()
    page.get_by_role("button", name="Dia inicial").click()

    page.locator("mat-form-field").filter(has_text="Até").get_by_label("Abrir calendário").click()
    page.get_by_role("button", name="Dia final").click()

    # Filtros e extração
    page.get_by_role("button").filter(has_text="Filtrar").click()
    page.locator("label").filter(has_text="Todos").locator("span").nth(1).click()
    time.sleep(1)

    page.get_by_role("button", name="Extrair Relatório").click()
    time.sleep(1)

    # Download do relatório
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Baixar CSV").click()
    download = download_info.value

    # Caminho genérico para salvar
    download.save_as("relatorio_sistema.csv")
    print(Fore.GREEN + "✅ Relatório gerado com sucesso. Verifique o arquivo 'relatorio_s
