from helpers.config import config_driver
from pages.job_page import JobPage
from models.job_data import Job


# TODO Можно вшить чанк с ссылками в класс при инициализации, но пока буду передавать извне

class JobsParser:
    def __init__(self):
        self.driver = config_driver()
        self.job_page = JobPage(self.driver)
        self.parsed_jobs: list[Job] = []


    def parse_jobs(self, links: list[str]):
        for i in range(len(links)):
            self._parse_one_job(links[i])
            print(f'Вакансия {i + 1} просмотрена')

        self.driver.quit()
        return self.parsed_jobs


    def _parse_one_job(self, link):
        self.job_page.open(link)
        job_data = Job(
            name=self.job_page.job_name,
            link=link,
            skills=self._collect_skills_from_job(),
            salary=self.job_page.salary,
            experience=self.job_page.experience,
            work_format=self.job_page.work_format
        )
        self.parsed_jobs.append(job_data.model_dump())


    def _collect_skills_from_job(self):
        skills: list[str] = []
        for skill in self.job_page.skills:
            skills.append(skill.text)
        return skills




class SkillsSorter:
    def get_all_sorted_skills(self, parsed_jobs):
        # TODO Вызов этой функции можно поместить в parse_jobs,
        #  а результат записывать в экземпляр.
        #  Потому что эту функцию нельзя вызывать до вызова parse_jobs
        unsorted_result: list[str] = []

        for job in parsed_jobs:
            for skill in job['skills']:
                unsorted_result.append(skill)

        sorted_skills = self._sort_skills(unsorted_result)
        return sorted_skills


    def _sort_skills(self, skills: list[str]):
        result = {}
        for skill in skills:
            if skill in result:
                result[skill] += 1
            if skill not in result:
                result[skill] = 1

        sorted_skills = sorted(result.items(), key=lambda x: x[1])[::-1]
        return sorted_skills