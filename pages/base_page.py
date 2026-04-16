from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    base_url = 'https://hh.ru/'


    def __init__(self, driver: WebDriver):
        self.driver= driver


    def open(self, url):
        self.driver.get(url)


    def find(self, args):
        return self.driver.find_element(*args)


    def find_all(self, args):
        return self.driver.find_elements(*args)


    def scroll_page_to_bottom(self):
        html = self.find((By.CSS_SELECTOR, 'html'))
        self.driver.execute_script(
            'window.scrollTo(0, 100000)',
            html
        )


    def quit(self):
        self.driver.quit()