from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
from configparser import ConfigParser
import cryptocode
from log import Log
import pyautogui
from time import sleep

class Functions:
    def __init__(self):
        self.log = Log()

    def Config(self, condition=''):
        try:
            self.config = ConfigParser()
            self.config.read('config.ini')
            self.url = self.config.get('PLATFORMS', 'url')
            self.user = cryptocode.decrypt(self.config.get('DADOS', 'user'), 'wow')
            self.password = cryptocode.decrypt(self.config.get('DADOS', 'password'), 'wow')
            if condition == 'User':
                return self.user
            elif condition == 'Password':
                return self.password
            else:
                return self.url
        except IOError as error:
            print('Config Error', error)

    def Json(self):
        try:
            with open(r".\Steps.json", "r") as json_file:
                Json_Steps = json.load(json_file)
                return Json_Steps

        except Exception as error:
            print('Json Error', error)
            Json_Steps = False
            return Json_Steps
            pass

    def Element(self, webdriver, find, element_html):
        try:
            if find == 'TAG_NAME':
                element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.TAG_NAME, element_html)))
            elif find == 'CLASS_NAME':
                element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, element_html)))
            elif find == 'CSS_SELECTOR':
                element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_html)))
            elif find == 'ID':
                element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.ID, element_html)))
            elif find == 'XPATH':
                element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, element_html)))
            else:
                return
            self.log.debug(f"Element {element_html} found!")
            print(f'Element found! -> {element_html}')
            return element
        except Exception as error:
            print('Element not found: ', error)



    def Actions(self, element, action, value, webdriver, wait, find):

        try:
            self.actions = ActionChains(webdriver)

            sleep(int(wait))
            if action == 'Digitar':
                element.clear()
                if value == 'User':
                    usuario = Functions().Config('User')
                    element.send_keys(usuario)
                elif value == 'Password':
                    senha = Functions().Config('Password')
                    element.send_keys(senha)
                else:
                    element.send_keys(valor)

            if action == 'Enter':
                self.actions.send_keys(Keys.ENTER).perform()

            if action == 'Click':
                if find == 'IMG':
                    img = pyautogui.locateOnScreen(value)
                    sleep(int(wait * 2))
                    pyautogui.moveTo(img)
                    sleep(int(wait * 2))
                    pyautogui.click()
                else:
                    self.actions.move_to_element(element)
                    self.actions.click(element).perform()

            if action == "Double_Click":
                self.actions.double_click(element).perform()

            self.log.debug(f"Action: '{action}' completed successfully.")
            print(f'Action: "{action}" completed successfully.')

        except Exception as error:
            print(f'Element error: {error}')








