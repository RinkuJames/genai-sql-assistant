from fastapi import APIRouter
from app.llm.sql_generator import generate_sql

router = APIRouter()

@router.post("/")
def run_query(payload: dict):
    question = payload.get("question")

    if not question:
        return {"error": "Question is required"}
    
    # Generate SQL using GenAI
    sql_query = generate_sql(question)

    return {
        "question": question,
        "generated_sql": sql_query
    }
