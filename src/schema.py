from pydantic import BaseModel
from typing import List

class MatchRequest(BaseModel):
    resume_text: str
    job_descriptions: List[str]

class MatchResponse(BaseModel):
    matches: List[str]
