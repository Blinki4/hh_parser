from models.job_data import Job
from pages.job_page import JobPage
from pages.search_page import SearchPage


class Parser:
    links: list[str] = []
    parsedJobsList: list[Job] = []

    def __init__(self, driver, query):
        self.query = query
        self.search_page = SearchPage(driver, self.query)
        self.job_page = JobPage(driver)
        self.search_page.open(self.search_page.url)

    def _get_pages_count(self) -> int:
        pages_count = self.search_page.get_pages_count()
        print(f'Всего найдено страниц: {pages_count}')
        return pages_count


    def get_links(self) -> None:
        self.links = self.search_page.collect_links(self._get_pages_count())
        print(f'Всего найдено вакансий: {len(self.links)}')


    def try_parse_jobs(self) -> list[Job]:
        try:
            return self._parse_jobs()
        except KeyboardInterrupt:
            print('Прервано... Промежуточные результаты сохранены в директории results')
            return self.parsedJobsList


    def _parse_jobs(self) -> list[Job]:
        for i in range(len(self.links)):
            self.job_page.open(self.links[i])
            job_data = Job(
                name=self.job_page.job_name,
                link=self.links[i],
                skills=self._get_skills_from_job(),
                salary=self.job_page.salary,
                experience=self.job_page.experience,
                work_format=self.job_page.work_format
            )
            self.parsedJobsList.append(job_data.model_dump())
            print(i + 1)
        return self.parsedJobsList

    def _get_skills_from_job(self) -> list[str]:
        skills: list[str] = []
        for skill in self.job_page.skills:
            skills.append(skill.text)
        return skills


    def get_job_skills(self, job_list: list[Job]):
        result: list[str] = []

        for link in job_list:
            for skill in link['skills']:
                result.append(skill)

        sorted_skills = self._sort_skills(result)
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