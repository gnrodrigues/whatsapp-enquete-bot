from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ===== CONFIGURAÇÕES =====

NOME_GRUPO = "GRUPO"

PERGUNTA = "Encontro?"

OPCOES = [
    "Vou",
    "Talvez",
    "Não vou"
]


# ===== INICIAR NAVEGADOR =====

options = webdriver.ChromeOptions()

options.add_argument("--remote-debugging-port=9222")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

# Perfil do Chrome para manter login
options.add_argument(r"--user-data-dir=C:\WhatsAppBotProfile")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://web.whatsapp.com")

wait = WebDriverWait(driver, 30)

print("⏳ Aguardando login no WhatsApp Web...")
time.sleep(20)


# ===== BUSCAR GRUPO =====

print("🔎 Buscando grupo...")

search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')

search_box.click()
search_box.send_keys(NOME_GRUPO)

time.sleep(3)

search_box.send_keys(Keys.ENTER)

time.sleep(2)


# ===== ABRIR CRIAR ENQUETE =====

print("📎 Abrindo menu de anexos...")

attach_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(@data-icon,"plus")]'))
)

attach_button.click()


poll_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[text()="Poll"]'))
)

driver.execute_script("arguments[0].click();", poll_button)

time.sleep(1)


# ===== PREENCHER PERGUNTA =====

print("❓ Inserindo pergunta...")

question_input = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
    )
)

question_input.send_keys(PERGUNTA)


# ===== FUNÇÃO PARA BUSCAR INPUTS =====

def get_poll_inputs():
    return wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@contenteditable="true"]')
        )
    )


# ===== INSERIR OPÇÕES =====

print("🗳️ Inserindo opções da enquete...")

for i, opcao in enumerate(OPCOES):

    inputs = get_poll_inputs()

    campo = inputs[i + 1]

    campo.click()
    campo.send_keys(opcao)

    time.sleep(0.5)


# ===== ENVIAR ENQUETE =====

print("🚀 Enviando enquete...")

send_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//div[@role="button" and @aria-label="Send"]')
    )
)

send_button.click()

time.sleep(5)

print("✅ Enquete enviada com sucesso!")

driver.quit()
