from helpers.config import config_driver
from pages.search_page import SearchPage


class LinksParser:
    def __init__(self, query):
        self.query = query
        self.driver = config_driver()
        self.search_page = SearchPage(self.driver, self.query)
        self.links: list[str] = []


    def collect_links(self) -> list[str]:
        self.open_search_page()
        self.links = self.search_page.collect_links(self._get_pages_count())
        print(f'Всего найдено вакансий: {len(self.links)}')
        self.close_search_page()
        return self.links


    def _get_pages_count(self) -> int:
        pages_count = self.search_page.get_pages_count()
        print(f'Всего найдено страниц: {pages_count}')
        return pages_count


    def open_search_page(self):
        self.search_page.open(self.search_page.url)


    def close_search_page(self):
        self.driver.quit()