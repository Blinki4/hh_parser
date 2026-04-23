from typing import Any
from parsers.jobs_parser import JobsParser

class ChunksManager:
    @staticmethod
    def split_list_into_chunks(array: list[Any], full_chunks_count) -> list[list[Any]]:
        full_chunk, remainder = divmod(len(array), full_chunks_count)
        all_chunks = []
        chunk = []
        for element in array:
            chunk.append(element)
            if len(chunk) == full_chunk:
                all_chunks.append(chunk)
                chunk = []
        if len(chunk) > 0:
            all_chunks.append(chunk)
        return all_chunks


    @staticmethod
    def parse_chunk(chunk):
        jobs_parser = JobsParser()
        parsed_jobs = jobs_parser.parse_jobs(chunk)
        return parsed_jobs


    @staticmethod
    def join_chunks(chunks: list[list[Any]]) -> list[Any]:
        result = []
        for chunk in chunks:
            for element in chunk:
                result.append(element)
        return result


if __name__ == '__main__':
    pass