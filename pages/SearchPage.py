from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.base_url + 'search/vacancy?ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&text=Qa+automation+python'

    ...