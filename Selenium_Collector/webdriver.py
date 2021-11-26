from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from seleniumwire import webdriver


class WebDriver:
    @staticmethod
    def getDriver():
        try:
            chrome_options = Options()                

            chrome_options.add_experimental_option(
                "prefs",
                {
                    "download.open_pdf_in_system_reader": False,
                    "download.prompt_for_download": False,
                    "download.default_directory": "/dev/null",
                    "plugins.always_open_pdf_externally": False,
                    "download_restrictions": 3,
                    "profile.default_content_setting_values.notifications": 2,
                },
            )
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument('--ignore-certificate-errors-spki-list')
            chrome_options.add_argument('--ignore-ssl-errors')

            web_driver = webdriver.Chrome(options=chrome_options)

            return web_driver

        except WebDriverException as WBE:
            print(WBE)
            pass
