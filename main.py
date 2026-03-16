import json

from pages.JobPage import JobPage
from pages.SearchPage import SearchPage


def main():
    search_page = SearchPage(query='qa automation python')
    search_page.open(search_page.url)
    search_page.write_links_in_file('links.txt')
    search_page.quit()

    result = []

    for link in search_page.links:
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

    print(result)

    with open('result.txt', 'w') as file:
        file.write(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()