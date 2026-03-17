from pages.JobPage import JobPage
from models.parsed_links import ParsedLink


def parse_links(links: list[str], page: JobPage) -> list[ParsedLink]:
    result: list[ParsedLink] = []
    for i in range(len(links)):
        page.open(links[i])

        skills: list[str] = []
        for skill in page.skills:
            skills.append(skill.text)

        job_data = ParsedLink(name=page.job_name, link=links[i], skills=skills)
        result.append(job_data.model_dump())
        print(i)
        # page.quit() # Не открывать каждый раз драйвер

    return result



if __name__ == '__main__':
    pass