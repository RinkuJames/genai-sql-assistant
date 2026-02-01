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

