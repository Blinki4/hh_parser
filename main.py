import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import json

def setup_driver() -> WebDriver:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def main():
    links = []
    driver = setup_driver()
    driver.get('https://hh.ru/search/vacancy?ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&text=Qa+automation+python')
    title_elements = driver.find_elements(By.XPATH, '//a[@data-qa="serp-item__title"]')
    with open('links.txt', 'w') as file:
        for el in title_elements:
            link = el.get_attribute('href')
            links.append(link)
            file.write(f'{link}\n')

    # driver.get('https://hh.ru/vacancy/131099127?query=Qa+automation+python&hhtmFrom=vacancy_search_list')
    # skills_elements = driver.find_elements(By.XPATH, '//li[@data-qa="skills-element"]')
    # skills = []
    # for skill in skills_elements:
    #     skills.append(skill.text)
    #     print(skill.text)
    # result[f'{link}'] = skills
    # print(result)
    result = {}
    for link in links:
        driver.get(link)
        skills_elements = driver.find_elements(By.XPATH, '//li[@data-qa="skills-element"]')
        skills = []
        for skill in skills_elements:
            skills.append(skill.text)
            print(skill.text)
        result[f'{link}'] = skills

    print(result)

    with open('result.txt', 'w') as file:
        file.write(json.dumps(result, indent=4))

    driver.quit()




if __name__ == '__main__':
    main()