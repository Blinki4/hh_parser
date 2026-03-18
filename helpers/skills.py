from models.job_data import JobData


def sort_skills(skills: list[str]):

    result = {}

    for skill in skills:
        if skill in result:
            result[skill] += 1
        if skill not in result:
            result[skill] = 1


    sorted_skills = sorted(result.items(), key=lambda x: x[1])[::-1]
    return sorted_skills


def get_all_skills(data: list[JobData]):
    result: list[str] = []

    for link in data:
        for skill in link['skills']:
            result.append(skill)


    sorted_skills = sort_skills(result)
    return sorted_skills

if __name__ == '__main__':
    pass