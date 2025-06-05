from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.extractor import extract_clauses
from app.summarizer import summarize_text

app = FastAPI(title="Legal Contract Analyzer")

class ContractRequest(BaseModel):
    text: str

@app.post("/extract_clauses")
def extract_contract_clauses(request: ContractRequest):
    clauses = extract_clauses(request.text)
    return {"clauses": clauses}

@app.post("/summarize")
def summarize_contract(request: ContractRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}
