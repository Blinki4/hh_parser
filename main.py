import sys
from parser.jobs_parser import JobsParser
from parser.links_parser import LinksParser
from writer.writer import Writer
from helpers.format_query import format_query
from helpers.lead_time import lead_time
from multiprocessing import Pool


# PROCESS_COUNT = 4

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

    jobs_parser = JobsParser()
    parsed_jobs = jobs_parser.parse_jobs(links)
    skills = jobs_parser.get_all_sorted_skills()
    #
    ###

    file_writer.write_job_data(parsed_jobs)
    file_writer.write_skills(skills)
    print('Результаты сформированы в директории results')


if __name__ == '__main__':
    main()