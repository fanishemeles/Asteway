from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def read_root():
    return {"message": "Welcome to Asteway AI"}

@app.post("/chat")
async def chat(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return {"response": response["choices"][0]["message"]["content"]}
