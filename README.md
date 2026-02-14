# genai-sql-assistant
A GenAI-powered assistant that converts natural language questions into optimized SQL queries over a data warehouse, executes them safely, and returns business-ready insights with explanations.

HIGH-LEVEL ARCHITECTURE

User Question
   ↓
  API
   ↓
Schema Retriever
   ↓
LLM Prompt Builder
   ↓
SQL Generator (GenAI)
   ↓
SQL Validator & Guardrails
   ↓
Warehouse Execution
   ↓
Result Summarizer (GenAI)
   ↓
Response    

TECH STACK

| Layer         | Tech                   |
| ------------- | ---------------------- |
| API           |                        |
| GenAI         |                        |
| Orchestration | Python                 |
| DB            | Postgres / Redshift    |
| Prompting     | LangChain              |
| Auth          | API Key                |
| Logging       | Python logging + table |


# APIs
<img width="975" height="422" alt="image" src="https://github.com/user-attachments/assets/c492a6c2-f0fb-4285-8773-a7d623c3c5a5" />

# Request - List all Customers
<img width="975" height="516" alt="image" src="https://github.com/user-attachments/assets/969bff65-48f2-492e-80f7-c468e7bc5b76" />

# Output Response
<img width="975" height="566" alt="image" src="https://github.com/user-attachments/assets/9b737f33-6683-42d7-876e-77b241c642c3" />

# Request - Show total sales by customer for last month
<img width="975" height="553" alt="image" src="https://github.com/user-attachments/assets/1b6a894a-7994-44c0-8423-6fbc379bf7f2" />

# Output Response
<img width="975" height="490" alt="image" src="https://github.com/user-attachments/assets/6c4fefb8-cdc9-4128-a2df-f0e873577b15" />



