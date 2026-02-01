from fastapi import FastAPI
from app.api.query import router as query_router

app = FastAPI(
    title="GenAI SQL Assistant",
    description="Natural language to SQL analytics assistant for data warehouses",
    version="0.1.0"
)

app.include_router(query_router, prefix="/query")

@app.get("/health")
def health_check():
    return {"status": "ok"}
