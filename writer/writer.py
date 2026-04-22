import os.path
from pathlib import Path
import json
from models.job_data import Job


class Writer:
    def __init__(self):
        self.home_path = Path(os.path.expanduser('~'))
        self.output_dir = self.home_path / 'Desktop' / 'results'
        self.output_dir.mkdir(exist_ok=True, parents=True)


    def write_links(self, links: list[str]) -> None:
        with open(self.output_dir / 'links.txt', 'w', encoding='utf-8') as file:
            for link in links:
                file.write(f'{link}\n')


    def write_skills(self, skills: list[tuple]):
        with open(self.output_dir / 'skills.txt', 'w') as file:
            for skill in skills:
                file.write(f'{skill[0]} = {skill[1]}\n')


    def write_job_data(self, data: list[Job]):
        with open(self.output_dir / 'data.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False))
