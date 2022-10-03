
import json
from time import sleep
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import *

#! REVISADO
#! REVISADO
#! REVISADO

def CreateDriver():
    print(3.1)
    chrome_options = selenium.webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-in-process-stack-traces")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('lang=en')
    chrome_options.add_argument("--output=/dev/null")
    chrome_options.add_argument("--no-sandbox")
    print(3.2)
    d = Chrome(executable_path='./chromedriver', options=chrome_options)
    print(3.3)
    d.set_window_size(int(1920/1.25), int(1080/1.25))
    print(3.4)
    return d



def LoadPage(url:str, webdriver:selenium.webdriver.Chrome, waitOnEnd:float=0.5):
    webdriver.get(url)
    WaitLoad(webdriver, waitOnEnd)


def WaitLoad(webdriver:selenium.webdriver.Chrome, waitOnEnd:float=0.5):
    load = False
    while(not load):
        try:
            sleep(0.2)
            load = str(webdriver.execute_script("return document.readyState;")) in "complete"
        except Exception as e:
            print("Deu erro na hora de esperar a página carregar")
    sleep(waitOnEnd)


# faz login em um dos bots
def Login(driver, cookie:str=None) -> bool:
    if DOMINIO not in driver.current_url :
        LoadPage(URL.SITE, driver)

    return load_cookie(driver, cookies=cookie)


def load_cookie(driver, cookies=None) -> bool:

    try:
        if(DOMINIO not in driver.current_url):
            LoadPage(URL.SITE, driver)
            
        cookies = json.loads(cookies)
        
        driver.delete_all_cookies()

        for cookie in cookies:
            driver.add_cookie(cookie)

        if(len(cookies) != 0):
            print("Cookies carregados")
            return True
        else:
            print("Não há cookies para serem carregados")
    except Exception as e:
        print("Erro na hora de carregar os cookies")
    return False