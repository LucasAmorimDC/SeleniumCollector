from Functions import Functions
from log import Log
from webdriver import WebDriver
import PySimpleGUI as sg
import json

Debug = True


class Main:

    def __init__(self):
        self.ind = 0
        self.log = Log()
        self.url = Functions().Config()
        self.webdriver = WebDriver().getDriver()
        self.webdriver.get(self.url)
        self.webdriver.maximize_window()
        self.dic_steps = dict()
        self.Json_File = Functions().Json()

        if self.Json_File:
            self.list_steps = self.Json_File[:]
            self.ind = len(self.Json_File)
            SeleniumActions().LoopDriver(self.log, self.webdriver)
        else:
            self.list_steps = list()

    def open_window(self):

        sg.theme('Dark Blue 2')
        layout = [[sg.Text('Action   '), sg.Combo(['Digitar', 'Enter', 'Click', 'Double_Click'], key='Action')],
                  [sg.Text('Find      '), sg.Combo(['TAG_NAME', 'CLASS_NAME', 'CSS_SELECTOR', 'ID', 'XPATH', 'IMG'], key='Find'),
                   sg.Text('Sleep   '), sg.Spin(['1', '2', '3', '4', '5'], key='Sleep')],
                  [sg.Text('Element'), sg.InputText(key='Element')],
                  [sg.Text('Value    '), sg.InputText(key='Value')],
                  [sg.Button('Save'), sg.Button('Delete')],
                  [sg.Output(size=(50, 7), key='-OUT-')]]

        window = sg.Window('Debug Selenium', layout)

        while True:
            self.event, self.values = window.read()
            if self.event == sg.WIN_CLOSED:
                break
            self.dic_steps['Action'] = self.values['Action']
            self.dic_steps['Sleep'] = self.values['Sleep']
            self.dic_steps['Find'] = self.values['Find']
            self.dic_steps['Element'] = self.values['Element']
            self.dic_steps['Value'] = self.values['Value']

            if self.event == 'Delete':
                self.list_steps.pop(-1)
                self.ind -= 1
                with open('Steps.json', 'w') as json_file:
                    json.dump(self.list_steps, json_file, indent=4)
                print('The last action successfully deleted!!')
                self.event = ''

            if self.event == 'Save':
                self.list_steps.append(self.dic_steps.copy())
                with open('Steps.json', 'w') as json_file:
                    json.dump(self.list_steps, json_file, indent=4)
                self.event = ''
                SeleniumActions().Driver(self.webdriver, self.log, self.ind)
                self.ind += 1


class SeleniumActions:

    def Driver(self, webdriver, log, ind):

        json_steps = Functions().Json()
        log.debug(f"")
        log.debug(f"--- Started Step {ind + 1}/{len(json_steps)} ---")
        print()
        print(f"        --- Started Step {ind + 1}.. ---")
        self.element = Functions().Element(webdriver, json_steps[ind]['Find'], json_steps[ind]['Element'])
        Functions().Actions(self.element, json_steps[ind]['Action'], json_steps[ind]['Value'], webdriver, json_steps[ind]['Sleep'], json_steps[ind]['Find'])

    def LoopDriver(self, log, webdriver):

        Json_File = Functions().Json()
        for ind, json_steps in enumerate(Json_File):
            log.debug(f"")
            log.debug(f"--- Started Step {ind + 1}/{len(Json_File)} ---")
            print()
            print(f"        --- Started Step {ind + 1}/{len(Json_File)} ---")
            self.element = Functions().Element(webdriver, json_steps['Find'], json_steps['Element'])
            Functions().Actions(self.element, json_steps['Action'], json_steps['Value'], webdriver, json_steps['Sleep'], json_steps['Find'])


if __name__ == "__main__":
    if Debug == True:
        Main().open_window()
    else:
        Main()
