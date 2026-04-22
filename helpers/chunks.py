from typing import Any

from parser.jobs_parser import JobsParser


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


def get_chunks_together(chunks: list[list[Any]]) -> list[Any]:
    result = []
    for chunk in chunks:
        for element in chunk:
            result.append(element)
    return result


def parse_chunk(chunk):
    jobs_parser = JobsParser()
    parsed_jobs = jobs_parser.parse_jobs(chunk)
    return parsed_jobs


if __name__ == '__main__':
    pass