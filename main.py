from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "SymbIAtk Cloud Backend Operante"}

@app.post("/process")
def process_message(message: Message):
    response = f"Recebido: {message.text}"
    return {"response": response"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
