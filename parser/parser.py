from helpers.config import config_driver
from models.job_data import Job
from pages.job_page import JobPage
from pages.search_page import SearchPage


# TODO Разделить парсер вакансий с парсером ссылок.
#  После сбора ссылок закрывать драйвер в пуле открывать драйвер, парсить чанк ссылок и закрывать драйвер
# Таким образом получится, что мы откроем 4 драйвера, каждый из которых парсит свой чанк, всю дату собирать в объект
# Потом 4 таких объекта объединить в один и вывести в файл


class Parser:
    def __init__(self, query, links):
        self.query = query
        self.driver = config_driver()
        # self.search_page = SearchPage(self.driver, self.query)
        self.job_page = JobPage(self.driver)
        # self.search_page.open(self.search_page.url)
        # self.links: list[str] = []
        self.links = links
        self.parsedJobsList: list[Job] = []

    # def _get_pages_count(self) -> int:
    #     pages_count = self.search_page.get_pages_count()
    #     print(f'Всего найдено страниц: {pages_count}')
    #     return pages_count
    #
    #
    # def collect_links(self) -> None:
    #     self.links = self.search_page.collect_links(self._get_pages_count())
    #     print(f'Всего найдено вакансий: {len(self.links)}')


    # def get_links(self):
    #     return self.links

    def try_parse_jobs(self) -> list[Job]:
        try:
            return self._parse_jobs()
        except KeyboardInterrupt:
            print('Прервано... Промежуточные результаты сохранены в директории results')
            return self.parsedJobsList


    def _parse_jobs(self) -> list[Job]:
        for i in range(len(self.links)):
            self._parse_one_job(self.links[i])
            print(i + 1)
        return self.parsedJobsList


    def _parse_one_job(self, link):
        self.job_page.open(link)
        job_data = Job(
            name=self.job_page.job_name,
            link=link,
            skills=self._get_skills_from_job(),
            salary=self.job_page.salary,
            experience=self.job_page.experience,
            work_format=self.job_page.work_format
        )
        self.parsedJobsList.append(job_data.model_dump())

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