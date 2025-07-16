from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS settings to allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify: ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str

# Dummy response function – you can update with real AI logic
# chatbot.py

def generate_response(message: str) -> str:
    """
    This function takes a user message and returns a response
    based on basic keyword matching logic.
    """
    message = message.lower()

    if "return" in message:
        return "Sure! I can help you with product returns."
    elif "refund" in message:
        return "I'll guide you through the refund process."
    elif "order" in message:
        return "Could you please provide your order ID?"
    elif "cancel" in message:
        return "I can assist you with canceling your order."
    elif "hi" in message or "hello" in message:
        return "Hello! How can I assist you today?"
    elif "price" in message or "cost" in message:
        return "Please let me know the product you're referring to."
    elif "thank" in message:
        return "You're welcome! Let me know if there's anything else."
    else:
        return "Thanks for contacting E-Cart! How can I assist you today?"

# API endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    reply = generate_response(request.message)
    return {"reply": reply}
