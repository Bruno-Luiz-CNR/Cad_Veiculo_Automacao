from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def pesquisar(placa):
    chrome = None  # Inicializa a variável chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    try:
        # Inicializar o driver do Chrome com as opções configuradas
        chrome = webdriver.Chrome(options=chrome_options)
        url_rotas = "https://siger.winksys.com.br:8443/#consultaveiculo"

        chrome.maximize_window()
        chrome.get(url_rotas)
        wait = WebDriverWait(chrome, 30)  # Aumente o tempo máximo de espera, se necessário

        usuario = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div[4]/form/'
                                                                         'div/div[1]/input')))
        usuario.send_keys("usuário")

        senha = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div[4]/form/'
                                                                       'div/div[2]/input')))
        senha.send_keys("senha")

        chrome.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div[4]/form/div/div[3]/button').click()

        # Aguardar até que o elemento esteja visível e clicável
        menu_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[5]/'
                                                                        'div[1]/div[1]')))
        menu_element.click()

        submenu_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[5]/div[1]/div[2]/a[18]')))
        submenu_element.click()

        ativa_todos = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div'
                                                                            '/div[2]/div[6]/select')))
        ativa_todos.send_keys("Todos")
        ativa_todos.send_keys(Keys.RETURN)

        input_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/input')))
        input_element.send_keys(placa)

        chrome.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[12]/button').click()

        placasistema = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/'
                                                        'table/tbody/tr[2]/td[2]/div')))

        if placasistema.text == placa:
            modelo = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/div'))).text
            ano = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[2]/td[5]/div'))).text
            cor = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[2]/td[6]/div'))).text
            chassi = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/div'))).text
            ren = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[2]/td[9]/div'))).text
            cliente = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[2]/td[11]/div'))).text
            return placa, modelo, ano, cor, chassi, ren, cliente, True
        else:
            chrome.quit()
            return None, None, None, None, None, None, None, False

    except Exception:
        chrome.quit()
        return False
    finally:
        if chrome is not None:
            chrome.quit()
