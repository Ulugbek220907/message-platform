from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(title="Message Platform")

# Allow requests from anywhere (adjust if you want to lock it down)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageIn(BaseModel):
    receiver: str
    name: str
    message: str

# In-memory store { receiver_id: [ {name, message, time}, ... ] }
STORE: dict[str, list[dict]] = {}

@app.get("/")
def root():
    return {"ok": True, "service": "message-platform"}

@app.post("/send")
def send_message(msg: MessageIn):
    payload = {"name": msg.name, "message": msg.message, "time": int(time.time() * 1000)}
    STORE.setdefault(msg.receiver, []).append(payload)
    return {"status": "Message sent!"}

@app.get("/messages/{receiver}")
def get_messages(receiver: str):
    return STORE.get(receiver, [])
