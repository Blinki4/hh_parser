from pages.job_page import JobPage
from models.job_data import JobData


def get_job_data(links: list[str], page: JobPage) -> list[JobData]:
    result: list[JobData] = []
    try:
        for i in range(len(links)):
            page.open(links[i])

            skills: list[str] = []
            for skill in page.skills:
                skills.append(skill.text)

            job_data = JobData(name=page.job_name, link=links[i], skills=skills)
            result.append(job_data.model_dump())
            print(i + 1)

        return result
    except KeyboardInterrupt:
        print('Прервано... Промежуточные результаты сохранены в директории results')
        return result


if __name__ == '__main__':
    pass