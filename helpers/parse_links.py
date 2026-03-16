from pages.JobPage import JobPage


def parse_links(links: list[str]): #TODO pydantic схема
    result = []
    for link in links:
        job_page = JobPage()
        job_page.open(link)

        job_data = {}
        job_data['link'] = link
        skills = []

        for skill in job_page.skills:
            skills.append(skill.text)
            print(skill.text)

        job_data['skills'] = skills
        result.append(job_data)
        job_page.quit()

    return result






if __name__ == '__main__':
    pass