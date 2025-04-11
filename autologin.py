from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.service import Service
from logger import logging

def autologin():
    try:
        service = Service('./chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.set_window_size(1000, 900)
        driver.get("http://social.sinergiatel.it.wifi/login")
        
        button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, "go"))
        )
        ActionChains(driver).move_to_element(button).click().perform()
        sleep(10)
        
        driver.quit()
    except Exception as e:
        print(f'ERROR - Errore login automatico: {e}')
        logging.error(f'Errore login automatico: {e}')
#by Riccardo Luongo, 17/08/2023
