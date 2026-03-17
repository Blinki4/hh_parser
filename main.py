import sys

from datetime import datetime

from pages.JobPage import JobPage
from pages.SearchPage import SearchPage
from helpers.write_results import write_links, write_results
from helpers.parse_links import parse_links
from helpers.skills import get_all_skills


def main():
    start = datetime.now()
    print(start)
    query = sys.argv[1]
    print('Идет поиск, не прерывайте выполнение программы')

    # links = get_job_links(query)
    search_page = SearchPage(query) # Открываем страницу, получаем кол-во страниц TODO: Заменять пробелы в поиске на +


    print('PAGES_COUNT', search_page.pages_count)

    for page in range(search_page.pages_count):
        # print(search_page.make_url(page))
        search_page.open(search_page.make_url(page))
        search_page.get_links()
        # print(page, search_page.links, len(search_page.links))
        print(f'Страница {page + 1} просмотрена')

    print('LINKS', search_page.links, len(search_page.links))

    job_page = JobPage()
    write_links(search_page.links)
    parsed_data = parse_links(search_page.links, job_page)
    skills = get_all_skills(parsed_data)

    write_results(parsed_data, skills)
    job_page.quit()
    print('Результаты сформированы в директории results')

    #Можно не делать пагинацию для скиллов, а просто открывать ссылки
    # Записывать в файл построчно, а не все разом

    end = datetime.now()
    print(end)

if __name__ == '__main__':
    main()