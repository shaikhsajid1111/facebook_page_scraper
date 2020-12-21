#!/usr/bin/env python
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
except ModuleNotFoundError:
    print("Please download dependencies")


class Initializer:

    def __init__(self,browser_name):
        self.browser_name = browser_name

    def set_properties(self,browser_option):
        browser_option.add_argument('--no-sandbox')
#        browser_option.add_argument('--headless')
        browser_option.add_argument("--disable-dev-shm-usage")
        browser_option.add_argument("disable-infobars")
        browser_option.add_argument('--ignore-certificate-errors')
        browser_option.add_argument('--disable-gpu')
        browser_option.add_argument('--log-level=3')
        browser_option.add_argument('--disable-notifications')
        browser_option.add_argument('--disable-popup-blocking')
        return browser_option

    def set_driver_for_browser(self,browser_name):
        if browser_name == "chrome":
            browser_option = ChromeOptions()
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=self.set_properties(browser_option))
        elif browser_name == "firefox":
            browser_option = FirefoxOptions()
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=self.set_properties(browser_option))
    
    def init(self):
        driver = self.set_driver_for_browser(self.browser_name)
        return driver
