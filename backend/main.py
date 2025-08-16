from fastapi import FastAPI, Request
from pydantic import BaseModel
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = FastAPI()

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your sheet (replace with your sheet name)
sheet = client.open("MessagePlatform").sheet1

class Message(BaseModel):
    receiver: str
    name: str
    message: str

@app.post("/send")
def send_message(msg: Message):
    # Save to Google Sheets
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([msg.receiver, msg.name, msg.message, now])

    # TODO: also handle delivering to Godot users (like before)
    return {"status": "Message saved and sent!"}

@app.get("/ping")
def ping():
    return {"status": "alive"}
