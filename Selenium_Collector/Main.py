from Functions import Functions
from log import Log
from webdriver import WebDriver
import PySimpleGUI as sg
import json


class Main:

    def __init__(self):

        self.ind = 0  # Indice utilizado para acessar o json.
        self.log = Log()  # Log de registro.
        self.url = Functions().Json('Collector', 'url')  # Url da plataforma.
        self.webdriver = WebDriver().getDriver()  # Options webdriver.
        self.webdriver.get(self.url)  # Get na url.
        self.Json_File = Functions().Json()  # Recebe o Steps_json.

        if self.Json_File['Steps']:  # Verificação para saber se o Steps_json está vazio .
            SeleniumActions().LoopDriver(self.log, self.webdriver)

    def open_window(self):

        sg.theme('Dark Blue 2')
        layout = [[sg.Text('Action   '),
                   sg.Combo(['Digitar', 'Enter', 'Click', 'Click_js', 'Double_Click', 'Iframe', 'IframeOFF', 'Link',
                             'Attribute_ID', 'set_class', 'Alert', 'New_Pag', 'Close', 'Refresh', 'Clear'],
                            key='Action'),
                   sg.Checkbox('Search_element', default=True, key='Search')],
                  [sg.Text('Find      '),
                   sg.Combo(['CSS_SELECTOR', 'ID', 'XPATH', 'Attribute_ID', 'Seletor_Js'],
                            key='Find'),
                   sg.Text('Sleep   '), sg.Spin(['0', '1', '2', '3', '4', '5'], key='Sleep')],
                  [sg.Text('Element'), sg.InputText(key='Element')],
                  [sg.Text('Value    '), sg.InputText(key='Value')],
                  [sg.Button('Save'), sg.Button('Delete')],
                  [sg.Output(size=(50, 7), key='-OUT-')]]

        window = sg.Window('Debug Selenium', layout)

        while True:
            self.event, values = window.read()
            if self.event == sg.WIN_CLOSED:
                break
            self.dic_steps = {
                "Search": f"{str(values['Search'])}",
                "Action": f"{values['Action']}",
                "Sleep": f"{values['Sleep']}",
                "Find": f"{values['Find']}",
                "Element": f"{values['Element']}",
                "Value": f"{values['Value']}"
            }

            if self.event == 'Delete':
                self.Json_File['Steps'].pop(-1)
                self.ind -= 1
                with open('Steps.json', 'w') as json_Steps:
                    json.dump(self.Json_File, json_Steps, indent=4)
                print('The last action successfully deleted!!')

            if self.event == 'Save':
                self.Json_File['Steps'].append(self.dic_steps)
                with open('Steps.json', 'w') as json_Steps:
                    json.dump(self.Json_File, json_Steps, indent=4)
                SeleniumActions().Driver(self.webdriver, self.log, self.ind)
                self.ind += 1

            self.event = ''


class SeleniumActions:
    def __init__(self):
        self.Json_Steps = Functions().Json('Steps')

    def Driver(self, webdriver, log, ind):

        log.debug(f"")
        log.debug(f"--- Started Step {ind + 1}/{len(self.Json_Steps)} ---")
        print()
        print(f"        --- Started Step {ind + 1}.. ---")
        if self.Json_Steps[ind]['Search'] == 'True':
            element = Functions().Element(webdriver, self.Json_Steps[ind]['Find'], self.Json_Steps[ind]['Element'])

        Functions().Actions(self.Json_Steps[ind]['Action'], self.Json_Steps[ind]['Value'],
                            webdriver, self.Json_Steps[ind]['Sleep'], element)

    def LoopDriver(self, log, webdriver):

        for ind, json_steps in enumerate(self.Json_Steps):
            log.debug(f"")
            log.debug(f"--- Started Step {ind + 1}/{len(self.Json_Steps)} ---")
            print()
            print(f"        --- Started Step {ind + 1}/{len(self.Json_Steps)} ---")
            if json_steps['Search'] == 'True':
                element = Functions().Element(webdriver, json_steps['Find'], json_steps['Element'])

            Functions().Actions(json_steps['Action'], json_steps['Value'], webdriver,
                                json_steps['Sleep'], element)


if __name__ == "__main__":
    Debug = Functions().Json('Collector', 'debug')
    if Debug == 'True':
        Main().open_window()
    elif Debug == 'False':
        Main()
