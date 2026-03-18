from pydantic import BaseModel


class JobData(BaseModel):
    name: str
    link: str
    skills: list[str]