import sys

from datetime import datetime

from pages.JobPage import JobPage
from pages.SearchPage import SearchPage
from helpers.write_results import write_links, write_results
from helpers.parse_links import parse_links
from helpers.skills import get_all_skills


def main():
    print(f'Started - {datetime.now()}')
    query = sys.argv[1]
    ###
    # Поиск ссылок на вакансии
    search_page = SearchPage(query) # Открываем страницу, получаем кол-во страниц TODO: Заменять пробелы в поиске на +
    search_page.open(search_page.url)
    print('Начался поиск, не прерывайте выполнение программы')
    pages = search_page.get_pages_count()
    print(f'Всего найдено страниц: {pages}')
    links = search_page.collect_links(pages)
    print(f'Всего найдено вакансий: {len(links)}')
    write_links(links)
    search_page.quit()
    # Конец поиска, закрытие драйвера
    ###
    # Начало парсинга скиллов
    job_page = JobPage()
    parsed_data = parse_links(links, job_page)
    skills = get_all_skills(parsed_data)
    write_results(parsed_data, skills)
    job_page.quit()
    print('Результаты сформированы в директории results')
    # Конец парсинга, закрытие драйвера
    ###

    print(f'End - {datetime.now()}')

if __name__ == '__main__':
    main()