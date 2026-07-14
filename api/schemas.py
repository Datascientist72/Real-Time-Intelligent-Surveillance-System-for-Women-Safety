from pydantic import BaseModel

class IncidentResponse(BaseModel):

    score: int

    level: str

    report: str