from pydantic import BaseModel


class Job(BaseModel):
    name: str
    link: str
    skills: list[str]
    salary: str
    experience: str
    work_format: str
    # TODO: Больше данных