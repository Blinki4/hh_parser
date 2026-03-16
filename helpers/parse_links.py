from pages.JobPage import JobPage
from models.parsed_links import ParsedLink


def parse_links(links: list[str]) -> list[ParsedLink]:
    result: list[ParsedLink] = []
    for link in links:
        job_page = JobPage()
        job_page.open(link)

        skills: list[str] = []
        for skill in job_page.skills:
            skills.append(skill.text)

        job_data = ParsedLink(link=link, skills=skills)
        result.append(job_data.model_dump())
        job_page.quit()

    return result



if __name__ == '__main__':
    pass