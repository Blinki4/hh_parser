from pydantic import BaseModel


class JobData(BaseModel):
    name: str
    link: str
    skills: list[str]
    salary: str
    experience: str
    work_format: str
    # TODO: Больше данных