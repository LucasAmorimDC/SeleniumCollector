from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Functions import Functions



class WebDriver:
    def getDriver(self):
        # _profile = neocript.get(coletor, "coletor", "profile")
        directory = Functions().Json('Collector', 'directory')
        chrome_options = Options()

        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": r"{}".format(directory),
            "profile.default_content_setting_values.automatic_downloads": 1,
            "download.Prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_argument("--window-size=100,50")
        # chrome_options.add_argument(f"--window-position=99999,0")
        chrome_options.add_argument("start-maximized")
        # chrome_options.add_argument("--user-data-dir={}".format(_profile))
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--no-sandbox")  # linux only
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-running-insecure-content')

        chrome_options.headless = False
        # if Functions().Json('Collector', 'headless') == 'True':
        #     chrome_options.headless = True

        return webdriver.Chrome(chrome_options=chrome_options)
