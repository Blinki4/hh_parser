from pydantic import BaseModel


class ParsedLink(BaseModel):
    link: str
    skills: list[str]