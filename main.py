import sys
from parser.jobs_parser import JobsParser
from parser.links_parser import LinksParser
from writer.writer import Writer
from helpers.format_query import format_query
from helpers.lead_time import lead_time
from multiprocessing import Process


links1 = [
    'https://hh.ru/vacancy/123631561?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131472414?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/128056006?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/128056139?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/123631559?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
]
links2 = [
    'https://hh.ru/vacancy/123608789?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/130639381?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131736442?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131998218?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/132112401?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list'
]
links3 = [
    'https://hh.ru/vacancy/131567149?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131713290?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131942090?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131747618?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131519345?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list'

]

links4 = [
    'https://hh.ru/vacancy/131953738?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/132225935?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/91986196?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/122157857?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/88127758?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list'
]
links5 = [
    'https://hh.ru/vacancy/88127777?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/131007399?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/130715947?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/123631560?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list',
    'https://hh.ru/vacancy/90599147?query=c+++reverse+engineer&hhtmFrom=vacancy_search_list'
]

# PROCESS_COUNT = 4
def parse(links_chunk):
    jobs_parser = JobsParser()
    parsed_jobs = jobs_parser.parse_jobs(links_chunk)
    print('PARSED_JOBS', parsed_jobs)
    skills = jobs_parser.get_all_sorted_skills()
    print('SKILLS', skills)

@lead_time
def main():
    query = format_query(sys.argv[1])
    file_writer = Writer()

    links_parser = LinksParser(query)
    links = links_parser.collect_links()

    # parser.collect_links()
    # links = parser.get_links() # МБ тут надо закрывать драйвер
    # links_chunk = int(len(links) / PROCESS_COUNT)
    # print(links_chunk, 'CHUNK')

    file_writer.write_links(links)
    ###
    # Этот блок запускать в разных процессах




    p1 = Process(target=parse, args=(links1,))
    p2 = Process(target=parse, args=(links2,))
    p3 = Process(target=parse, args=(links3,))
    p4 = Process(target=parse, args=(links4,))
    p5 = Process(target=parse, args=(links5,))


    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    #
    ###

    # file_writer.write_job_data(parsed_jobs)
    # file_writer.write_skills(skills)
    # print('Результаты сформированы в директории results')


if __name__ == '__main__':
    main()