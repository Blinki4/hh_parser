from models.parsed_links import ParsedLink


def get_all_skills(data: list[ParsedLink]) -> list[str]:
    result: list[str] = []

    for link in data:
        for skill in link['skills']:
            result.append(skill)

    return result


def sort_skills(skills: list[str]):

    result = {}

    for skill in skills:
        if skill in result:
            result[skill] += 1
        if skill not in result:
            result[skill] = 1


    sorted_skills = sorted(result.items(), key=lambda x: x[1])[::-1]
    return sorted_skills

if __name__ == '__main__':
    pass