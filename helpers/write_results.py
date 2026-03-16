import json

from models.parsed_links import ParsedLink
from pathlib import Path


def write_results(data: list[ParsedLink], skills: list[tuple]):
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)

    print('data:', data)
    print('skills:', skills)

    with open(output_dir / 'data.txt', 'w') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))


    with open(output_dir / 'skills.txt', 'w') as file:
        for skill in skills:
            file.write(f'{skill[0]} = {skill[1]}\n')

if __name__ == '__main__':
    pass