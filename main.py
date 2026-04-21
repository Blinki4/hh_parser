import sys
import json
from parser.jobs_parser import JobsParser
from parser.links_parser import LinksParser
from writer.writer import Writer
from helpers.format_query import format_query
from helpers.lead_time import lead_time
from multiprocessing import Process, Queue, Pool
from typing import Any



PROCESS_COUNT = 5 # Пиздеж

def split_list_into_chunks(array: list[Any], full_chunks_count) -> list[list[Any]]:
    full_chunk, remainder = divmod(len(array), full_chunks_count)
    all_chunks = []
    chunk = []
    for element in array:
        chunk.append(element)
        if len(chunk) == full_chunk:
            all_chunks.append(chunk)
            chunk = []
    all_chunks.append(chunk) # Если их все таки кратное количество, тут может быть пустой массив, потенциальная ошибка
    return all_chunks


def parse_chunk(links_chunk):
    jobs_parser = JobsParser()
    parsed_jobs = jobs_parser.parse_jobs(links_chunk)
    return parsed_jobs


@lead_time
def main():
    query = format_query(sys.argv[1])
    file_writer = Writer()

    links_parser = LinksParser(query)
    links = links_parser.collect_links()


    file_writer.write_links(links)


    chunks = split_list_into_chunks(links, PROCESS_COUNT)

    print(json.dumps(chunks, indent=4), 'CHUNKS')
    print(len(chunks), 'chunks count')



    # processes = []
    # for i in chunks:
    #     process = Process(target=parse_chunk, args=(i,))
    #     process.start()
    #     processes.append(process)
    #
    #
    # for p in processes:
    #     p.join()


    with Pool(len(chunks)) as pool:
        result = pool.map(parse_chunk, chunks)
        print(result)

    full = []

    for chunk in result:
        for job in chunk:
            full.append(job)


    jobs_parser = JobsParser()

    file_writer.write_job_data(full)
    skills = jobs_parser.get_all_sorted_skills(full)
    file_writer.write_skills(skills)

    print('Результаты сформированы в директории results')


if __name__ == '__main__':
    main()