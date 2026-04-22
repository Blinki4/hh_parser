class ProcessPool:
    """
    Запускает парсинг вакансий в нескольких процессах
    (Жестко нарушает принцип единой ответственности)
    """
    def __init__(self, processes_count, links):
        self.processes_count = processes_count
        self.links = links


    def split_links_into_chunks(self, full_chunks_count) -> list[list[str]]:
        full_chunk, remainder = divmod(len(self.links), full_chunks_count)
        all_chunks = []
        chunk = []
        for element in self.links:
            chunk.append(element)
            if len(chunk) == full_chunk:
                all_chunks.append(chunk)
                chunk = []
        all_chunks.append(chunk)
        # ^
        # |
        # Если их все таки кратное количество, тут может быть пустой массив, потенциальная ошибка
        return all_chunks