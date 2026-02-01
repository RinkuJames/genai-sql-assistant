from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from app.llm.prompt_builder import build_prompt
from gpt4all import GPT4All

import os

# Ensure you have your OPENAI_API_KEY in .env
import dotenv
dotenv.load_dotenv()

# Load GPT4All local model (small, free local model)
model = GPT4All("ggml-gpt4all-j-v1.3-groovy")

#llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)    #Incurs Cost

#Function to generate sql for the user's question
def generate_sql(question: str) -> str:
    """
    Generates SQL from natural language question using GPT4All (free, local model)
    """
     # Build schema-aware prompt
    prompt = build_prompt(question)
    prompt += f"\n\nQuestion: {question}\nGenerate a safe SQL SELECT query only."

    #chat_prompt = ChatPromptTemplate.from_template("{text}")
    #response = llm(chat_prompt.format_prompt(text=prompt).to_messages())
    #sql_query = response[0].content if hasattr(response[0], "content") else str(response)
    # Generate SQL using GPT4All
    sql_query = model.generate(prompt, n_predict=256)  # n_predict limits response length

    return sql_query
