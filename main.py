import sys

from parser.parser import Parser
from writer.writer import Writer
from helpers.format_query import format_query
from helpers.config import config_driver
from helpers.lead_time import lead_time

@lead_time
def main():
    query = format_query(sys.argv[1])
    driver = config_driver()
    parser = Parser(driver, query)
    writer = Writer()
    links = parser.get_links()
    writer.write_links(links)
    jobs_data = parser.get_jobs(links)
    skills = parser.get_job_skills(jobs_data)
    writer.write_job_data(jobs_data)
    writer.write_skills(skills)
    print('Результаты сформированы в директории results')
    driver.quit()


if __name__ == '__main__':
    main()