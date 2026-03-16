import json

from pages.SearchPage import SearchPage
from helpers.parse_links import parse_links


def main():
    search_page = SearchPage(query='qa automation python')
    search_page.open(search_page.url)
    search_page.write_links_in_file('links.txt')
    search_page.quit()

    result = []

    result = parse_links(search_page.links)
    print(result)

    with open('result.txt', 'w') as file:
        file.write(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()