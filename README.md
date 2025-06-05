# Legal Contract Analyzer 🔍

This project provides a FastAPI-based API that:
- Extracts key clauses (dates, parties, obligations) from legal contracts using spaCy.
- Summarizes long legal documents using a transformer-based model.

### How to Run Locally
```bash
uvicorn app.main:app --reload
