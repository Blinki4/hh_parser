import sys

from pages.SearchPage import SearchPage


def main():

    query = sys.argv[1]
    print('Идет поиск, не прерывайте выполнение программы')

    # links = get_job_links(query)
    search_page = SearchPage(query) # Открываем страницу, получаем кол-во страниц TODO: Заменять пробелы в поиске на +
    # parsed_data = parse_links(search_page.links)
    # skills = get_all_skills(parsed_data)

    # write_results(parsed_data, skills)


    print('PAGES_COUNT', search_page.pages_count)

    for page in range(search_page.pages_count):
        # print(search_page.make_url(page))
        search_page.open(search_page.make_url(page))
        search_page.get_links()
        # print(page, search_page.links, len(search_page.links))
        print(f'Страница {page + 1} просмотрена')

    print('LINKS', search_page.links, len(search_page.links))

    print('Результаты сформированы в папке results')


if __name__ == '__main__':
    main()