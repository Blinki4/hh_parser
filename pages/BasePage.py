from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    base_url = 'https://hh.ru/'


    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        self.driver: WebDriver = driver


    def open(self, url):
        self.driver.get(url)


    def find(self, args):
        return self.driver.find_element(*args)


    def find_all(self, args):
        return self.driver.find_elements(*args)


    def quit(self):
        self.driver.quit()