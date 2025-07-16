from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str

# Real AI response using OpenAI ChatGPT
def generate_response(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini-2024-07-18:jkkn-institutions::AkU4LoFv",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant for an e-commerce platform called E-Cart."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, an error occurred: {str(e)}"

# API endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    reply = generate_response(request.message)
    return {"reply": reply}
