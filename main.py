import sys

from parser.parser import Parser
from writer.writer import Writer
from helpers.format_query import format_query
from helpers.config import config_driver
from helpers.lead_time import lead_time


PROCESS_COUNT = 4

@lead_time
def main():
    query = format_query(sys.argv[1])
    # driver = config_driver()
    # parser = Parser(driver, query)
    parser = Parser(query)
    writer = Writer()

    parser.collect_links()
    links = parser.get_links() # МБ тут надо закрывать драйвер
    links_chunk = int(len(links) / PROCESS_COUNT)
    print(links_chunk, 'CHUNK')

    writer.write_links(parser.links)
    jobs_data = parser.try_parse_jobs()
    skills = parser.get_job_skills(jobs_data)
    writer.write_job_data(jobs_data)
    writer.write_skills(skills)
    print('Результаты сформированы в директории results')
    parser.driver.quit()


if __name__ == '__main__':
    main()