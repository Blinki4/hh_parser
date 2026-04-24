from writers.writer import Writer
import csv

class CsvWriter(Writer):

    def write_parsed_jobs(self, parsed_jobs):
        field_names = ['name', 'salary', 'experience', 'work_format', 'skills', 'link']
        with open(self.output_dir / 'result.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(parsed_jobs)



if __name__ == '__main__':
    pass