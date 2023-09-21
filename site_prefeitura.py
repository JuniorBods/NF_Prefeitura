from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from datetime import datetime
import calendar
from tkinter import filedialog
import os
import streamlit as st

''' 1 - TERMINAR DE SEPARAR AS FUNÇÕES
    2 - CRIAR A FUNÇÃO PARA MOSTRAR AS EMPRESAS E DEIXAR ELE SELECIONAR
    3 - CRIAR A FUNÇÃO PARA ARMAZENAR O LOGIN EM UM ARQUIVO JSON
    4 - PERGUNTAR QUAL O CAMINHO SALVAR OS ARQUIVOS
    5 - CRIAR LAYOUT NO STREAMLIT'''
    
# usuario = '78396409234'
# senha = 'asc756321'

usuario = st.text_input("Usuario")
senha = st.text_input("Senha", type='password')

pasta_raiz = filedialog.askdirectory()


mes = datetime.now().month-1
mes2 = str(mes).zfill(2) 
ano = datetime.now().year
dia = calendar.monthrange(ano,mes)[1]

# chrome_options = Options()
# chrome_options.add_argument("--headless")
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': r'D:\SCI - Sistema Contabil',
    'download.prompt_for_download': False,
    'plugins.always_open_pdf_externally': True
})

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://nfse.ji-parana.ro.gov.br/issweb/paginas/login"
navegador.maximize_window()
navegador.get(url)
navegador.implicitly_wait(30)


empresas_inativas = ['assis','agrospeed']

def login_site():
    try:
        navegador.find_element('xpath', '//*[@id="username"]').send_keys(f"{usuario}")
        navegador.find_element('xpath', '//*[@id="password"]').send_keys(f"{senha}")
    except:
        print("Elemento não encontrado")
        navegador.refresh()

    sleep(2)
    navegador.find_element('xpath', '//input[@type="submit"]').click()
 
    
def pesquisar():
    navegador.find_element('xpath', '//*[@id="form:btnDefault"]/span[2]').click()
    sleep(4)


def pega_numero_empresas():
    numero_empresas = navegador.find_elements('class name','ui-commandlink')
    for x in range(len(numero_empresas)):
        if x >= 1:
            navegador.find_element('xpath', '//*[@id="form:btnDefault"]/span[2]').click()
            sleep(4)
        else:
            pass
    
    nome = navegador.find_element('xpath', f'//*[@id="form:listaContribuintes_data"]/tr[{x+1}]/td[3]').text
    nome = nome.split(' ')[0:5]
    nome = ' '.join(nome)
    print(nome)
    sleep(2)
    for y in empresas_inativas:
        if y.upper() in nome:
            print("Empresa inativa")
        else:
            
            # If nome estiver na lista de exclusão pula o codigo
            caminho = rf'{pasta_raiz}\{nome}\NFSe\{ano}\{mes2}-{ano}'
            caminho_arquivo = f'{nome}-{mes2}-{ano}.pdf'
            # Verifica se a pasta existe
            if not os.path.exists(caminho):
                # Cria a pasta
                os.makedirs(caminho)
                print("Pasta criada com sucesso!")
                
            elif not caminho_arquivo in os.listdir(caminho):
                navegador.find_element('xpath', f'//*[@id="form:listaContribuintes:{x}:j_idt513"]/img').click()
                sleep(2)
                navegador.find_element('xpath', '//*[@id="navNfse"]').click()
                sleep(2)
                navegador.find_element('xpath', '//*[@id="navConNfs"]').click()
                sleep(2)
                navegador.find_element('xpath', '//*[@id="form:dtInicio_input"]').clear()
                sleep(2)
                navegador.find_element('xpath', '//*[@id="form:dtInicio_input"]').send_keys(f"01/{mes2}/{ano}")
                sleep(2)
                navegador.find_element('xpath', '//*[@id="form:dtFim_input"]').clear()
                sleep(2)
                navegador.find_element('xpath', '//*[@id="form:dtFim_input"]').send_keys(f"{dia}/{mes2}/{ano}")
                sleep(2)
                navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                navegador.find_element('xpath', '//*[@id="form:cbPesquisar"]').click()
                sleep(2)
                navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                try:
                    navegador.find_element('xpath', '//*[@id="form:cbImprimirButton"]').click()
                    sleep(4)
                    # Encontre a posição do botão de download zip na tela e repetir o processo
                    navegador.find_element('xpath', '//*[@id="sidebar-left"]').click()
                    sleep(2)
                    navegador.execute_script("window.scrollTo(0, 0);")
                    sleep(2)
                    navegador.find_element('xpath', '//*[@id="navCnt"]').click()
                    sleep(2)
                    navegador.find_element('xpath', '//*[@id="j_idt88:linkSelecionarContribuinte"]').click()
                    sleep(2)
                except:
                    print('Sem Notas Fiscais para serem geradas')
            else:
                print('Arquivo Existente')
                

if __name__ == '__main__':
    login_site()