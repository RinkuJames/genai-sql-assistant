import json

def build_prompt(question: str, schema_path: str = "schemas/warehouse_schema.json") -> str:
    """
    Constructs a prompt for the LLM that includes the warehouse schema.
    """
    try:
        with open(schema_path, "r") as f:
            schema = json.load(f)
    except FileNotFoundError:
        schema = {"tables": {}, "columns": {}}

    prompt = f"""
You are a SQL expert. Given the following warehouse schema:
{json.dumps(schema, indent=2)}

Convert the following natural language question into a valid SQL query.
Question: "{question}"
Rules:
- Only generate SELECT statements
- Use table and column names exactly as in schema
- Do not include destructive operations (DROP, DELETE, UPDATE)
- Assume standard SQL syntax
"""
    return prompt
