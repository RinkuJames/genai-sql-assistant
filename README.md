# genai-sql-assistant
A GenAI-powered SQL query generator that converts natural language questions into optimized SQL queries using a free, local LLM, which can be used over a data warehouse. This project is implemented using GenAI(LLM Model) deployed in the local, Python and FastAPI.

# FEATURES
Convert natural language questions into SQL queries.
Schema-aware SQL generation: respects table and column names from a JSON file named warehouse_schema.json.
Free, local LLM (Meta LLaMA 3.1 8B) for no API costs. (Note: The model is not included in the repo due to size limits.)
FastAPI backend with Swagger UI for testing API endpoints.
Modular Python project structure for easy extension and maintenance.

# TECHNOLOGIES USED
Python 3.12+
FastAPI (API backend)
Meta-Llama-3.1-8B-Instruct-Q4_K_S.gguf (local LLM for SQL generation, placed in app/llm/models/)
LangChain (prompt building & structuring)


# HIGH-LEVEL ARCHITECTURE (HOW IT WORKS)

User Question Input (Natural language SQL question)
    ↓   
   API
    ↓
Schema Retriever (Reads warehouse_schema.json)
    ↓
LLM Prompt Builder
    ↓
SQL Generator by LLM from the prompt(Gen AI)    
    ↓
API Response: returns SQL query in JSON

# COMMAND FOR RUNNING API 
uvicorn app.main:app --reload
Open http://127.0.0.1:8000/docs to test via Swagger UI


# APIs
<img width="975" height="422" alt="image" src="https://github.com/user-attachments/assets/c492a6c2-f0fb-4285-8773-a7d623c3c5a5" />

# LIST ALL CUSTOMERS
# Request : POST /query 
{
  "question": "List all customers"
}
# Response
{
  "question": "List all customers",
  "generated_sql": "SELECT customer_id, name, email, country FROM customers;"
}

<img width="975" height="516" alt="image" src="https://github.com/user-attachments/assets/969bff65-48f2-492e-80f7-c468e7bc5b76" />

# Output Response
<img width="975" height="566" alt="image" src="https://github.com/user-attachments/assets/9b737f33-6683-42d7-876e-77b241c642c3" />


# Show total sales by customer for last month
# Request : POST /query 
{
  "question": "Show total sales by customer for last month"
}
# Response
{
  "question": "Show total sales by customer for last month",
  "generated_sql": "SELECT c.customer_id, c.name, SUM(o.total_amount) AS total_sales FROM customers c JOIN orders o ON                          c.customer_id = o.customer_id WHERE o.order_date >= DATEADD(MONTH, -1, CURRENT_DATE) GROUP BY                               c.customer_id, c.name ORDER BY total_sales DESC;"
}


<img width="975" height="553" alt="image" src="https://github.com/user-attachments/assets/1b6a894a-7994-44c0-8423-6fbc379bf7f2" />

# Output Response
<img width="975" height="490" alt="image" src="https://github.com/user-attachments/assets/6c4fefb8-cdc9-4128-a2df-f0e873577b15" />


