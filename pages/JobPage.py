from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class JobPage(BasePage):

    skill_selector = (By.XPATH, '//li[@data-qa="skills-element"]')

    def __init__(self):
        super().__init__()


    @property
    def skills(self):
        return self.find_all(self.skill_selector)

