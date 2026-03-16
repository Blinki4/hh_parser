from pydantic import BaseModel


class ParsedLink(BaseModel):
    name: str
    link: str
    skills: list[str]