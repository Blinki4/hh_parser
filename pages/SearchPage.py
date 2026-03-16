from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):

    job_title_selector = (By.XPATH, '//a[@data-qa="serp-item__title"]')
    links = []

    def __init__(self, query):
        super().__init__()
        self.url = self.base_url + f'search/vacancy?ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&text={query}'


    @property
    def job_titles(self):
        return self.find_all(self.job_title_selector)


    def write_links_in_file(self, path):
        with open(path, 'w') as file:
            for el in self.job_titles:
                link = el.get_attribute('href')
                file.write(f'{link}\n')
                self.links.append(link)