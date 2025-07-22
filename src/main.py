from fastapi import FastAPI, HTTPException
from src.schemas import MatchRequest, MatchResponse
from src.model import match_resumes

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/match", response_model=MatchResponse)
def match(request: MatchRequest):
    try:
        results = match_resumes(request.resume_text, request.job_descriptions)
        return {"matches": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
