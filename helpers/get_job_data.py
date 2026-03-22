from pages.job_page import JobPage
from models.job_data import JobData


def get_job_data(links: list[str], job_page: JobPage) -> list[JobData]:
    result: list[JobData] = []
    try:
        for i in range(len(links)):
            job_page.open(links[i])

            skills: list[str] = []
            for skill in job_page.skills:
                skills.append(skill.text)

            job_data = JobData(
                name=job_page.job_name,
                link=links[i],
                skills=skills,
                salary=job_page.salary,
                experience=job_page.experience,
                work_format=job_page.work_format
            )
            result.append(job_data.model_dump())
            print(i + 1)

        return result
    except KeyboardInterrupt:
        print('Прервано... Промежуточные результаты сохранены в директории results')
        return result


if __name__ == '__main__':
    pass