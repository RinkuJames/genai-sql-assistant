#from langchain.chat_models import ChatOpenAI
#from langchain.prompts import ChatPromptTemplate
from app.llm.prompt_builder import build_prompt
from gpt4all import GPT4All

import os

# Ensure you have your OPENAI_API_KEY in .env
#import dotenv
#dotenv.load_dotenv()

# Load GPT4All local model (small, free local model)
#model = GPT4All("ggml-gpt4all-j-v1.3-groovy")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models")
MODEL_NAME = "Meta-Llama-3.1-8B-Instruct-Q4_K_S.gguf"
model = GPT4All(model_name=MODEL_NAME, model_path=MODEL_PATH, allow_download=False, n_threads=4)

#llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)    #Incurs Cost

#Function to generate sql for the user's question
def generate_sql(question: str) -> str:
    """
    Generates SQL from natural language question using GPT4All (free, local model)
    """
    # Build schema-aware prompt
    prompt = build_prompt(question)
    #prompt += f"\n\nQuestion: {question}\nGenerate a safe SQL SELECT query only."
    prompt += """
    IMPORTANT RULES (MUST FOLLOW):
    - Return ONLY ONE SQL SELECT statement
    - Do NOT include markdown (```sql)
    - Do NOT include comments
    - Do NOT include explanations
    - Do NOT include multiple queries
    - End with a semicolon (;)

    SQL:
    """
    
    #chat_prompt = ChatPromptTemplate.from_template("{text}")
    #response = llm(chat_prompt.format_prompt(text=prompt).to_messages())
    #sql_query = response[0].content if hasattr(response[0], "content") else str(response)
    # Generate SQL using GPT4All
    result_query = model.generate(prompt, n_predict=128, temp=0.1)  # n_predict limits response length

    sql = result_query.strip()
     # Remove markdown if model ignored instructions
    sql = sql.replace("```sql", "").replace("```", "")

    # Keep only first SELECT statement
    if "SELECT" in sql.upper():
        sql = sql.upper().split("SELECT", 1)[1]  # everything after first SELECT
        sql = "SELECT " + sql
        sql = sql.split(";")[0] + ";"  # keep only first semicolon

    return sql    
