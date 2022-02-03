from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from log import Log
import cryptocode
import json
import os


class Functions:
    def __init__(self):
        self.log = Log()
        self._directory = self.Json('Collector', 'directory')

    def Json(self, req1=None, req2=None):
        try:
            with open(r".\Steps.json", "r") as json_file:
                Json_Steps = json.load(json_file)

                if req1 is None:
                    return Json_Steps
                elif req1 == 'Steps':
                    return Json_Steps[req1]
                elif req1 == 'Login':
                    return cryptocode.decrypt(Json_Steps[req1][0][req2], 'wow')
                else:
                    return Json_Steps[req1][0][req2]
        except Exception as error:
            print('Json Error', error)
            return Json_Steps
            pass

    def Element(self, webdriver, find, element_html):

        try:

            if find == 'CSS_SELECTOR':
                element = WebDriverWait(webdriver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, element_html)))
            elif find == 'ID':
                element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.ID, element_html)))
            elif find == 'XPATH':
                element = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, element_html)))
            elif find == 'Attribute_ID':
                element = webdriver.execute_script(f"return document.getElementById('{element_html}')")
            elif find == 'Seletor_Js':
                element = webdriver.execute_script(f"return document.querySelector('{element_html}')")
            else:
                return
            self.log.debug(f"Element {element_html} found!")
            print(f'Element found! -> {element_html}')
            return element
        except Exception as error:
            print('Element not found: ', error)

    def Actions(self, action, value, webdriver, wait, element=None):

        try:
            self.actions = ActionChains(webdriver)
            sleep(int(wait))
            if element:
                self.actions.move_to_element(element)

            if action == 'Link':
                webdriver.get(value)

            """ Ação para abrir uma nova aba na URL desejada """
            if action == 'New_Pag':
                url = value
                webdriver.execute_script(f"window.open('{url}', 'new_window')")

            if action == 'Close':
                webdriver.close()

            if action == 'Refresh':
                webdriver.refresh()

            if action == 'Iframe':
                webdriver.switch_to.frame(element)

            elif action == 'IframeOFF':
                webdriver.switch_to.default_content()

            if action == 'set_class':
                webdriver.execute_script(f"arguments[0].setAttribute('class', '{value}')", element)

            if action == 'Digitar':
                element.clear()
                if value == 'User':
                    user = Functions().Json('Login', 'user')
                    element.send_keys(user)
                elif value == 'Pass':
                    password = Functions().Json('Login', 'pass')
                    element.send_keys(password)
                else:
                    element.send_keys(value)

            if action == 'Enter':
                self.actions.send_keys(Keys.ENTER).perform()

            if action == "Click_js":
                webdriver.execute_script("arguments[0].click();", element)

            # def multiple_file_types(self, *patterns):
            #     os.chdir(r"{}".format(self._directory))
            #     return it.chain.from_iterable(glob.iglob(pattern) for pattern in patterns)

            if action == 'Click':
                self.actions.click(element).perform()

            if action == "Attribute_ID":
                el_href = element.get_attribute('href')
                webdriver.execute_script(f"window.open('{el_href}', 'new_window')")

            """ Ação para aceitar alerta do navegador """
            if action == "Alert":
                WebDriverWait(webdriver, 3).until(EC.alert_is_present(),
                                                  'Tempo limite esgotado ao aguardar a presença do alerta' +
                                                  'pop-up de confirmação para aparecer.')

                alert = webdriver.switch_to.alert
                alert.accept()

            if action == 'Clear':
                for file in os.listdir(self._directory):
                    print(file, value)
                    if file == value:
                        os.remove(fr"{self._directory}/{file}")

            self.log.debug(f"Action: '{action}' completed successfully.")

            if action == "Download":
                Download = True
                while Download:
                    for file in os.listdir(self._directory):
                        if file[:12] == 'Hagent Login':
                            os.chdir(r"{}".format(self._directory))
                            os.rename(fr"{self._directory}/{file}", value)
                            Download = False

            print(f'Action: "{action}" completed successfully.')
        except Exception as error:
            print('Action error: ', error)
