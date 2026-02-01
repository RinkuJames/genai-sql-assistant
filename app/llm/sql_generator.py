from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from app.llm.prompt_builder import build_prompt
import os

# Ensure you have your OPENAI_API_KEY in .env
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

#Function to generate sql for the user's question
def generate_sql(question: str) -> str:
    prompt = build_prompt(question)
    chat_prompt = ChatPromptTemplate.from_template("{text}")
    response = llm(chat_prompt.format_prompt(text=prompt).to_messages())
    sql_query = response[0].content if hasattr(response[0], "content") else str(response)
    return sql_query
