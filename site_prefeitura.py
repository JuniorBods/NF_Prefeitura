from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from datetime import datetime
import calendar
import pyautogui
import os

usuario = '78396409234'
senha = 'asc756321'

mes = datetime.now().month-1
mes2 = str(mes).zfill(2) 
ano = datetime.now().year
dia = calendar.monthrange(ano,mes)[1]

url = "https://nfse.ji-parana.ro.gov.br/issweb/paginas/login"
servico = Service(ChromeDriverManager().install())

# chrome_options = Options()
# chrome_options.add_argument("--headless")
empresas_inativas = ['assis','agrospeed']
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()
pagina = navegador.get(url)
navegador.implicitly_wait(3)

try:
    navegador.find_element('xpath', '//*[@id="username"]').send_keys(f"{usuario}")
    navegador.find_element('xpath', '//*[@id="password"]').send_keys(f"{senha}")
except:
    print("Elemento não encontrado")
sleep(2)
navegador.find_element('xpath', '//*[@id="j_idt110"]').click()
sleep(2)
navegador.find_element('xpath', '//*[@id="form:btnDefault"]/span[2]').click()
sleep(4)

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
            caminho = rf'D:\SCI - Sistema Contabil\{nome}\NFSe\{ano}\{mes2}-{ano}'
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
                sleep(1)
                navegador.find_element('xpath', '//*[@id="navConNfs"]').click()
                sleep(2)
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
                sleep(2)
                try:
                    navegador.find_element('xpath', '//*[@id="form:cbImprimirButton"]').click()
                    sleep(4)
                    # Encontre a posição do botão de download na tela
                    posicao_botao = pyautogui.locateOnScreen('bt_download.png', confidence=0.7)
                    if posicao_botao is None:
                        print("Botão de download não encontrado.")
                    else:
                        centro_botao = pyautogui.center(posicao_botao)
                        x, y = centro_botao
                        pyautogui.moveTo(x, y)
                        pyautogui.click()
                    sleep(2)
                    # Encontre a posição do caminho do arquivo na tela
                    posicao_botao = pyautogui.locateOnScreen('caminho.png', confidence=0.7)
                    if posicao_botao is None:
                        print("Botão de download não encontrado.")
                    else:
                        centro_botao = pyautogui.center(posicao_botao)
                        x, y = centro_botao
                        pyautogui.moveTo(x, y)
                        pyautogui.click()
                    sleep(2)
                    pyautogui.typewrite(caminho)
                    sleep(1)
                    pyautogui.press('enter')
                    sleep(2)
                    # Encontre a posição do caminho do arquivo na tela
                    posicao_botao = pyautogui.locateOnScreen('nome_arquivo.png', confidence=0.7)
                    if posicao_botao is None:
                        print("Botão de download não encontrado.")
                    else:
                        centro_botao = pyautogui.center(posicao_botao)
                        x, y = centro_botao
                        pyautogui.moveTo(x, y)
                        pyautogui.doubleClick()
                    sleep(1)
                    pyautogui.typewrite(caminho_arquivo)
                    sleep(2)
                    pyautogui.press('enter')
                    sleep(5)
                    navegador.switch_to.window(navegador.window_handles[1])
                    navegador.close()
                    navegador.switch_to.window(navegador.window_handles[-1])
                    sleep(2)
                    # Encontre a posição do botão de download zip na tela e repetir o processo
                    navegador.find_element('xpath', '//*[@id="sidebar-left"]').click()
                    sleep(1)
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
    pass