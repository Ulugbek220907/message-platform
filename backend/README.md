# Message Platform (FastAPI)

Minimal backend for sending and receiving messages by numeric Receiver ID.

## Endpoints
- `POST /send`  — body `{ "receiver": "12345678", "name": "Alice", "message": "Hi" }`
- `GET /messages/{receiver}` — returns list of messages

## Run locally
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Then open http://127.0.0.1:8000
