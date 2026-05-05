import csv
from writers.writer import Writer


class CsvWriter(Writer):
    def __init__(self):
        super().__init__()
        self.headers_mapping = {
            'name' : 'Название',
            'salary' : 'Зарплата',
            'experience' : 'Опыт работы',
            'work_format' : 'Формат работы',
            'skills' : 'Ключевые навыки',
            'link' : 'Ссылка'
        }
        self.translated_keys = []


    def write_parsed_jobs(self, parsed_jobs):
        translated = self.translate_keys(parsed_jobs)
        with open(self.output_dir / 'result.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=self._make_field_names())
            writer.writeheader()
            writer.writerows(translated)


    def _make_field_names(self):
        field_names = []
        for key, value in self.headers_mapping.items():
            field_names.append(value)
        return field_names


    def translate_keys(self, parsed_jobs):
        for job in parsed_jobs:
            self.translate_key(job)
        return self.translated_keys


    def translate_key(self, job):
        translated_job = {}
        for key, value in job.items():
            translated_job[self.headers_mapping[key]] = value
        self.translated_keys.append(translated_job)

if __name__ == '__main__':
    pass