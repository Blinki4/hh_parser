from pages.SearchPage import SearchPage


def get_job_links(query):
    search_page = SearchPage(query=query)
    search_page.open(search_page.url)
    links = search_page.get_links()
    search_page.quit()
    return links