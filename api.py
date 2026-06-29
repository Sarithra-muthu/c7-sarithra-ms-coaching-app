from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from main import analyse_work

app = FastAPI()


class AnalyseRequest(BaseModel):
    subject: str
    work_content: str = Field(min_length=1)


class AnalyseResponse(BaseModel):
    subject: str
    feedback: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyse", response_model=AnalyseResponse)
def analyse(request: AnalyseRequest):
    try:
        feedback = analyse_work(request.subject, request.work_content)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return AnalyseResponse(subject=request.subject, feedback=feedback)
