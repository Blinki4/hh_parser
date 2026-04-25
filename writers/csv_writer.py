import csv
from writers.writer import Writer
from models.job import Job

class CsvWriter(Writer):
    def __init__(self):
        super().__init__()
        self.mapping = {
            'name' : 'Название',
            'salary' : 'Зарплата',
            'experience' : 'Опыт работы',
            'work_format' : 'Формат работы',
            'skills' : 'Ключевые навыки',
            'link' : 'Ссылка'
        }


    def write_parsed_jobs(self, parsed_jobs):
        translated = self.translate_keys(parsed_jobs)
        with open(self.output_dir / 'result.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=self._make_field_names())
            writer.writeheader()
            writer.writerows(translated)


    def _make_field_names(self):
        field_names = []
        for key, value in self.mapping.items():
            field_names.append(value)
        return field_names


    def translate_keys(self, parsed_jobs):
        translated = []
        for job in parsed_jobs:
            translated_job = {}
            for key, value in job.items():
                translated_job[self.mapping[key]] = value
            translated.append(translated_job)
        return translated


if __name__ == '__main__':
    pass