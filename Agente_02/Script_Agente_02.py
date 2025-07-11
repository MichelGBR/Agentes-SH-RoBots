import time
import os
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:

    usuario = os.getenv("APP_USUARIO")
    senha = os.getenv("APP_SENHA")

    if not usuario or not senha:
        raise ValueError("Credenciais não encontradas. Configure as variáveis de ambiente APP_USUARIO e APP_SENHA.")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.seusistema.com/login") 

    page.get_by_role("textbox", name="Usuário").fill(usuario)
    time.sleep(1)
    page.get_by_role("textbox", name="Senha").fill(senha)
    time.sleep(1)
    page.get_by_role("button", name="Iniciar sessão").click()
    time.sleep(1)

    page.get_by_role("menuitem", name="Gestão").click()
    time.sleep(1)
    page.get_by_role("menuitem", name="Financeiro").click()
    time.sleep(2)
    page.get_by_role("menuitem", name="Extrato").click()
    time.sleep(9)

    frame = page.locator("iframe[name=\"appArea\"]").content_frame
    frame.get_by_role("cell", name="Extrato", exact=True).click()
    time.sleep(5)
    frame.get_by_role("cell", name="Categoria", exact=True).click()
    time.sleep(2)
    frame.get_by_role("textbox", name="Saldo").dblclick()
    time.sleep(2)

    valor = frame.get_by_role("textbox", name="Saldo").input_value()
    print("Valor atual:", valor)

with sync_playwright() as playwright:
    run(playwright)
