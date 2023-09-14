from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import calendar

usuario = '78396409234'
senha = 'asc756321'

mes = datetime.now().month-1
mes2 = str(mes).zfill(2) 
ano = datetime.now().year
dia = calendar.monthrange(ano,mes)[1]


servico = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()
pagina = navegador.get("https://nfse.ji-parana.ro.gov.br/issweb/paginas/login")
navegador.implicitly_wait(3)

try:
    navegador.find_element('xpath', '//*[@id="username"]').send_keys(f"{usuario}")
    navegador.find_element('xpath', '//*[@id="password"]').send_keys(f"{senha}")
except:
    print("Elemento não encontrado")
sleep(2)
navegador.find_element('xpath', '//*[@id="j_idt110"]').click()
sleep(3)
navegador.find_element('xpath', '//*[@id="form:btnDefault"]/span[2]').click()
sleep(2)

numero_empresas = navegador.find_elements('class name','ui-commandlink')
for x in range(len(numero_empresas)):
    navegador.find_element('xpath', f'//*[@id="form:listaContribuintes:{x}:j_idt513"]/img').click()
    sleep(3)
    navegador.find_element('xpath', '//*[@id="navNfse"]').click()
    sleep(1)
    navegador.find_element('xpath', '//*[@id="navConNfs"]').click()
    sleep(3)
    navegador.find_element('xpath', '//*[@id="form:dtInicio_input"]').clear()
    sleep(1)
    navegador.find_element('xpath', '//*[@id="form:dtInicio_input"]').send_keys(f"01/{mes2}/{ano}")
    sleep(1)
    navegador.find_element('xpath', '//*[@id="form:dtFim_input"]').clear()
    sleep(1)
    navegador.find_element('xpath', '//*[@id="form:dtFim_input"]').send_keys(f"{dia}/{mes2}/{ano}")
    sleep(1)
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    navegador.find_element('xpath', '//*[@id="form:cbPesquisar"]').click()
    sleep(2)
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    navegador.find_element('xpath', '//*[@id="form:cbImprimirButton"]').click()
    sleep(2)
    navegador.find_element('xpath', '//*[@id="download"]').click()
    sleep(1)
    campo_ativo = navegador.switch_to.active_element.send_keys("nosso")
    #falta montar o caminho onde vai salvar o pdf com o nome da empresa automatico
    #e depois voltar e fazer o download do zip para a mesma pasta
    #depois voltar e trocar o contribuinte e fazer tudo de novo
    
input("Pressione Enter para sair...")


if __name__ == '__main__':
    pass