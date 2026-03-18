import json

from models.job_data import JobData
from pathlib import Path


def write_links(links: list[str]) -> None:
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / 'links.txt', 'w') as file:
        for link in links:
            file.write(f'{link}\n')

def write_results(data: list[JobData], skills: list[tuple]):
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)


    with open(output_dir / 'data.txt', 'w') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))


    with open(output_dir / 'skills.txt', 'w') as file:
        for skill in skills:
            file.write(f'{skill[0]} = {skill[1]}\n')



if __name__ == '__main__':
    pass