from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class JobPage(BasePage):

    skill_selector = (By.XPATH, '//li[@data-qa="skills-element"]')
    job_name_selector = (By.XPATH, '//h1[@data-qa="vacancy-title"]')

    def __init__(self):
        super().__init__()


    @property
    def skills(self):
        return self.find_all(self.skill_selector)


    @property
    def job_name(self):
        return self.find(self.job_name_selector).text