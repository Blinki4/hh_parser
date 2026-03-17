from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):

    job_title_selector = (By.XPATH, '//a[@data-qa="serp-item__title"]')
    pages_count_selector = (By.XPATH, '//li[@data-qa="number-pages-ellipsis"]/following::a[@data-qa="pager-page"]')
    page_selector = (By.XPATH, '//a[@data-qa="pager-page"]')

    links = []

    def __init__(self, query):
        super().__init__()
        self.current_page = 0
        self.url = self.base_url + f'search/vacancy?text={query}&page={self.current_page}&ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true'
        self.open(self.url)
        self.pages_count = self.get_pages_count()

    @property
    def job_titles(self):
        return self.find_all(self.job_title_selector)


    def get_links(self):
        # for page in self.pages_count:
        #     self.open()
        for el in self.job_titles:
            link = el.get_attribute('href')
            self.links.append(link)


    def get_pages_count(self) -> int:
        """
        Вызывается при инциициализации
        Возвращает количество страниц в поиске,
        """
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true);',
            self.job_titles[-1]
            )
        # self.scroll_page_to_bottom()
        try:
            pages = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(self.page_selector)
                )
            print(pages)
            return int(pages[-1].text)

        except TimeoutException:
            return 0