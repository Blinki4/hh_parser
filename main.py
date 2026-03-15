import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def setup_driver() -> WebDriver:
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def main():
    print('hello world!')
    driver = setup_driver()
    driver.get('https://hh.ru/search/vacancy?ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&text=Qa+automation+python')
    time.sleep(4)
    driver.quit()




if __name__ == '__main__':
    main()