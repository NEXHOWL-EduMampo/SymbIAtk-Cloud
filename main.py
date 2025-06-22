from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "SymbIAtk Cloud Backend Operante"}

@app.post("/process")
def process_message(message: Message):
    response = f"Recebido: {message.text}"
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
