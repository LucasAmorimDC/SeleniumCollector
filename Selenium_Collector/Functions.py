from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from configparser import ConfigParser
from bs4 import BeautifulSoup
from time import sleep
from log import Log
import pandas as pd
import cryptocode
import pyautogui
import json
import glob
import os



class Functions:
    def __init__(self):
        self.log = Log()

    def Config(self, req1, req2):
        try:
            self.config = ConfigParser()
            self.config.read('config.ini')
            request = self.config.get(req1, req2)
            if req1 == 'DADOS':
                request = cryptocode.decrypt(self.config.get(req1, req2), 'wow')
            return request
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
            if action == 'Insert':
                Functions().BulkInsert()
            if action == 'Extract':
                Functions().Extract(webdriver, element, value)
            if action == 'Digitar':
                element.clear()
                if value == 'User':
                    user = Functions().Config('DADOS', 'User')
                    element.send_keys(user)
                elif value == 'Password':
                    password = Functions().Config('DADOS', 'Password')
                    element.send_keys(password)
                else:
                    element.send_keys(value)

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
            print('Action error: ', error)


    def Extract(self, webdriver, element, value):

        try:
            if not os.path.exists("./Extract/"):
                os.mkdir("./Extract/")
            Class = element.get_attribute('class')
            tag = Functions().Config('CONTENT', 'tag')
            url = webdriver.page_source
            soup = BeautifulSoup(url, 'lxml')
            element = soup.find(tag, attrs={Class})
            df = pd.read_html(str(element))
            df[0].to_csv(f'./Extract/{value}.csv', header=False, index=False, mode='a', encoding='UTF-8', sep=',')
            print(df)
        except Exception as error:
            print('Extract error ', error)


    def BulkInsert(self):

        try:
            for file in glob.glob(f"./Extract/*.csv"):
                os.system(f'bcp {Functions().Config("SQL", "database")}.'
                          f'dbo.{Functions().Config("SQL", "table")} '
                          f'IN {file} -c -C 65001 -t "," -r 0x0a '
                          f'-S {Functions().Config("SQL", "server")} '
                          f'-U {Functions().Config("SQL", "user")} '
                          f'-P {Functions().Config("SQL", "pass")}'
                          )
                print(f'{file}: Successfully imported')
        except Exception as error:
            print('Insert error: ', error)

