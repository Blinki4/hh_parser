import sys
from parser.jobs_parser import JobsParser, SkillsSorter
from parser.links_parser import LinksParser
from writer.writer import Writer
from helpers.format_query import format_query
from helpers.lead_time import lead_time
from multiprocessing import Pool
from helpers.chunks import split_list_into_chunks, get_chunks_together, parse_chunk


FULL_CHUNKS_COUNT = 5 # Враки



@lead_time
def main():
    query = format_query(sys.argv[1])
    file_writer = Writer()
    links_parser = LinksParser(query)
    links = links_parser.collect_links()
    file_writer.write_links(links)

    chunks = split_list_into_chunks(links, FULL_CHUNKS_COUNT)


    with Pool(len(chunks)) as pool:
        parsed_jobs = pool.map(parse_chunk, chunks)


    result_data = get_chunks_together(parsed_jobs)
    sorter = SkillsSorter()
    file_writer.write_job_data(result_data)
    skills = sorter.get_all_sorted_skills(result_data)
    file_writer.write_skills(skills)

    print('Результаты сформированы в директории results')


if __name__ == '__main__':
    main()