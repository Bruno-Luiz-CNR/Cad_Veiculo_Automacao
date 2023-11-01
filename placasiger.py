import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def inseDados(placa, modelo, ano, cor, chassi, ren, cliente, equip):
    url_rotas = "https://tracking.systemsatx.com.br/Veiculo"
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(url_rotas)

    # url_rotas = "https://tracking.systemsatx.com.br/Veiculo"

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")

    # chrome = webdriver.Chrome(options=chrome_options)
    # chrome.maximize_window()
    # chrome.get(url_rotas)

    wait = WebDriverWait(chrome, 15)  # Aumente o tempo máximo de espera, se necessário
    usuarios = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="txtUsername"]/div/div[1]/input')))
    time.sleep(1)
    usuarios.send_keys("central3@cllick.com.br")

    senhas = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="txtSenha"]/div/div[1]/input')))
    senhas.send_keys("Blftgpds1@")

    chrome.find_element(By.XPATH, '//*[@id="btnSenha"]').click()

    placa_ssx = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="grid"]/div/div[5]/div/table/tbody/'
                                                                       'tr[2]/td[8]/div/div[2]/div/div/div[1]/input')))
    placa_ssx.send_keys(placa)
    placa_ssx.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        consulta_placa = chrome.find_element(By.XPATH, '//*[@id="grid"]/div/div[6]/div/div/div[1]/div/'
                                                       'table/tbody/tr[1]/td[5]').text
        if consulta_placa != placa:
            telacad = wait.until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="grid"]/div/div[4]/div/div/div[3]/div[3]/div/div')))
            telacad.click()

            divide = cliente.split(" - ")
            try:
                frames = chrome.find_elements(By.TAG_NAME, 'iframe')
                if frames:
                    for frame in frames:
                        chrome.switch_to.frame(frame)
                        try:
                            if len(divide) > 1:

                                aposTraco = divide[1].split()[:1]
                                cliente_traco = " ".join(aposTraco)

                                dadosClientess = wait.until(ec.visibility_of_element_located(
                                    (By.XPATH, '//*[@id="Cliente"]/div[1]/div/div[1]/input')))
                                dadosClientess.send_keys(cliente_traco)
                                time.sleep(1)
                                dadosClientess.send_keys(Keys.RETURN)

                                dadosOrganizacional = chrome.find_element(
                                    By.XPATH, '//*[@id="UnidadeOrganizacional"]/div/div/div[1]/input')
                                dadosOrganizacional.send_keys(cliente_traco)
                                time.sleep(1)
                                dadosOrganizacional.send_keys(Keys.RETURN)

                                chrome.find_element(
                                    By.XPATH, '//*[@id="identificacao"]/div/div[1]/input').send_keys(placa)

                                inse_moldelo = chrome.find_element(
                                    By.XPATH, '//*[@id="ModeloVeiculo"]/div/div/div[1]/input')
                                inse_moldelo.send_keys(modelo)
                                time.sleep(1)
                                inse_moldelo.send_keys(Keys.RETURN)
                                time.sleep(2)
                                informacoes = ano.replace(" ", "")
                                mode_fab = informacoes.split('/')
                                if len(mode_fab) == 2:
                                    ano = mode_fab[0]
                                    fab = mode_fab[1]
                                    chrome.find_element(
                                        By.XPATH, '//*[@id="AnoModelo"]/div/div[1]/input').send_keys(ano)
                                    chrome.find_element(
                                        By.XPATH,'//*[@id="AnoFabricacao"]/div/div[1]/input').send_keys(fab)
                                    chrome.find_element(
                                        By.XPATH, '//*[@id="NumeroChassi"]/div/div[1]/input').send_keys(chassi)
                                    chrome.find_element(
                                        By.XPATH,'//*[@id="NumeroRenavam"]/div/div[1]/input').send_keys(ren)
                                    chrome.find_element(
                                        By.XPATH, '//*[@id="Placa"]/div/div[1]/input').send_keys(placa)
                                    chrome.find_element(
                                        By.XPATH, '//*[@id="CorVeiculo"]/div/div[1]/input').send_keys(cor)
                                    chrome.find_element(By.XPATH, '//*[@id="listaAcao-salvar"]/div').click()

                                    chrome.find_element(By.XPATH, '//*[@id="2032"]/a/i').click()
                                    time.sleep(3)
                                    chrome.find_element(By.XPATH, '//*[@id="buttonAddEndereco"]/div/i').click()
                                    time.sleep(1)
                                    verificar_equip = chrome.find_element(
                                        By.XPATH, '//*[@id="Rastreador"]/div/div/div[1]/input')
                                    verificar_equip.send_keys(equip)
                                    time.sleep(2)
                                    verificar_equip.send_keys(Keys.RETURN)
                                    chrome.find_element(By.XPATH, '//*[@id="contentPopUpRastreador'
                                                                  'Formulario-listaAcao-salvar--inline"]'
                                                                  '/div/span').click()

                                    time.sleep(3)
                                    chrome.find_element(By.XPATH, '//*[@id="listaAcao-salvarFechar"]/div').click()
                                    time.sleep(5)
                                    chrome.quit()
                                    return True
                        except NoSuchElementException:
                            pass
                        finally:
                            chrome.switch_to.default_content()
                            return True
            except Exception as e:
                chrome.quit()
                raise Exception(f"Erro ao processar linha: {e}")
        else:
            chrome.quit()
    except Exception as e:
        raise Exception(f"Erro ao processar linha: {e}")
    finally:
        chrome.quit()


# Função para executar a automação em uma thread separada
def automacao_thread(placa, modelo, ano, cor, chassi, ren, cliente, equip):
    automation_thread = threading.Thread(target=inseDados, args=(placa, modelo, ano, cor, chassi, ren, cliente, equip))
    automation_thread.start()
