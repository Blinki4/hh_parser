from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class JobPage(BasePage):
    skill_selector = (By.XPATH, '//li[@data-qa="skills-element"]')
    job_name_selector = (By.XPATH, '//h1[@data-qa="vacancy-title"]')
    salary_selector = (By.XPATH, '//div[@data-qa="vacancy-salary"]')
    experience_selector = (By.XPATH, '//span[@data-qa="vacancy-experience"]')
    work_format_selector = (By.XPATH, '//p[@data-qa="work-formats-text"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def skills(self):
        return self.find_all(self.skill_selector)

    @property
    def job_name(self):
        return self.find(self.job_name_selector).text

    @property
    def salary(self):
        try:
            return self.find(self.salary_selector).text
        except NoSuchElementException:
            return 'Не указано'

    @property
    def experience(self):
        try:
            return self.find(self.experience_selector).text
        except NoSuchElementException:
            return 'Не указано'

    @property
    def work_format(self):
        try:
            return self.find(self.work_format_selector).text.replace('Формат работы: ', '')
        except NoSuchElementException:
            return 'Не указано'