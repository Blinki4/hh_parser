from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    job_title_selector = (By.XPATH, '//a[@data-qa="serp-item__title"]')
    page_selector = (By.XPATH, '//a[@data-qa="pager-page"]')

    def __init__(self, driver: WebDriver, query: str):
        super().__init__(driver)
        self.query: str = query
        self.url: str = self.make_url()

    @property
    def job_titles(self):
        return self.find_all(self.job_title_selector)

    def make_url(self, page: int = 0):
        return self.base_url + f'search/vacancy?text={self.query}&page={page}&ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true'

    def get_pages_count(self) -> int:
        """
        Возвращает количество страниц в поиске
        """
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true);',
            self.job_titles[-1]
            )
        try:
            pages = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(self.page_selector)
                )
            return int(pages[-1].text)
        except TimeoutException:
            return 0

    def collect_links(self, pages: int) -> list[str]:
        """
        Открывает каждую страницу поиска
        и собирает все ссылки на вакансии
        :param pages: Количество страниц
        :return: Массив ссылок на вакансию
        """

        links: list[str] = []

        def get_links():
            self.scroll_page_to_bottom()
            # time.sleep(1) # Пока не трогать
            for el in self.job_titles:
                link = el.get_attribute('href')
                links.append(link)

        if pages > 0:
            for page in range(pages):
                self.open(self.make_url(page))
                get_links()
        else:
            self.open(self.url)
            get_links()
        return links