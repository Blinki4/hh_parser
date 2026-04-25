import csv
from writers.writer import Writer
from models.job import Job

class CsvWriter(Writer):

    def write_parsed_jobs(self, parsed_jobs):
        field_names = ['Название', 'Зарплата', 'Опыт работы', 'Формат работы', 'Ключевые навыки', 'Ссылка']
        mapping = {
            'name' : 'Название',
            'salary' : 'Зарплата',
            'experience' : 'Опыт работы',
            'work_format' : 'Формат работы',
            'skills' : 'Ключевые навыки',
            'link' : 'Ссылка'
        }

        # TODO в цикле пройтись по mapping и составить field_names из значений, чтоб избежать связности

        translated = []
        for job in parsed_jobs:
            translated_job = {}
            for key, value in job.items():
                translated_job[mapping[key]] = value
            translated.append(translated_job)


        with open(self.output_dir / 'result.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(translated)



if __name__ == '__main__':
    pass