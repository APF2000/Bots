import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--js-flags=--expose-gc")

chrome_options.add_argument("--window-size=1920,1080")

import json

url_login = "https://edisciplinas.usp.br/acessar/"

logica_comp = "https://edisciplinas.usp.br/mod/attendance/view.php?id=4001185"
url_presenca = logica_comp 

credentials = json.load(open('login.json'))
email = credentials['email']
psswd = credentials['senha']

while(True):

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    #driver.maximize_window()

    driver.get(url_login)
    access = driver.find_element_by_xpath("//a[contains(., 'Acessar')]/i")
    
    try:
        access.click()
    except selenium.common.exceptions.ElementNotInteractableException:
        print("Not interactable")
        driver.close()
        continue

    in_email = driver.find_element_by_xpath("//label[@for='username']/../input")
    in_psswd = driver.find_element_by_xpath("//label[@for='password']/../input")

    in_email.send_keys(email)
    in_psswd.send_keys(psswd)

    submit = driver.find_element_by_xpath("//button[contains(., 'Login')]")
    submit.click()

    #time.sleep(60)

    driver.get(url_presenca)

    try:
        presenca = driver.find_element_by_xpath("//a[contains(., 'Registrar presença')]")
        presenca.click()
        print('Presença contabilizada')
        break
    except selenium.common.exceptions.NoSuchElementException:
        print("Presença ainda não disponível")
        pass

    time.sleep(60)
    driver.close()
    print("Espere um minuto")
    time.sleep(60)
