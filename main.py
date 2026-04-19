import sys

from parser.jobs_parser import JobsParser
from parser.links_parser import LinksParser
from parser.parser import Parser
from writer.writer import Writer
from helpers.format_query import format_query
from helpers.config import config_driver
from helpers.lead_time import lead_time


PROCESS_COUNT = 4

@lead_time
def main():
    query = format_query(sys.argv[1])
    links_parser = LinksParser(query)
    writer = Writer()

    # parser.collect_links()
    # links = parser.get_links() # МБ тут надо закрывать драйвер
    # links_chunk = int(len(links) / PROCESS_COUNT)
    # print(links_chunk, 'CHUNK')

    links = links_parser.collect_links()
    writer.write_links(links)
    ###
    #Этот блок запускать в разных процессах
    jobs_parser = JobsParser()
    parsed_jobs = jobs_parser.parse_jobs(links)
    skills = jobs_parser.get_all_sorted_skills()
    ###
    writer.write_job_data(parsed_jobs)
    writer.write_skills(skills)
    print('Результаты сформированы в директории results')


if __name__ == '__main__':
    main()