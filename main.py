import sys

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from pages.job_page import JobPage
from pages.search_page import SearchPage
from helpers.write_results import write_links, write_results
from helpers.get_job_data import get_job_data
from helpers.skills import get_all_skills

def config_driver() -> WebDriver:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

def main():
    print(f'Start: {datetime.now()}')
    query = sys.argv[1]

    driver = config_driver()
    ###
    # Поиск ссылок на вакансии
    search_page = SearchPage(driver, query) # TODO: Заменять пробелы в поиске на +
    search_page.open(search_page.url)
    print('Начался поиск, не прерывайте выполнение программы')
    pages = search_page.get_pages_count()
    print(f'Всего найдено страниц: {pages}')
    links = search_page.collect_links(pages)
    print(f'Всего найдено вакансий: {len(links)}')
    write_links(links)
    # Конец поиска, закрытие драйвера
    ###
    # Начало парсинга скиллов
    job_page = JobPage(driver)
    jobs_data = get_job_data(links, job_page)
    skills = get_all_skills(jobs_data)
    write_results(jobs_data, skills)
    print('Результаты сформированы в директории results')
    # Конец парсинга, закрытие драйвера
    ###
    print(f'End: {datetime.now()}')
    driver.quit()
if __name__ == '__main__':
    main()