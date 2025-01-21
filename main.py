from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import fila
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

queue_patient = fila.HospitalQueue()
app = FastAPI()

# Model to each item in the JSON
class Item(BaseModel):
    name: str
    age: float
    urgency: str

# Model to the json
class ItemList(BaseModel):
    items: List[Item]

# Endpoint main
@app.get("/")
def read_root():
    return {"message": "Welcome! :3"}

# Create a list of items
@app.post("/items/")
def create_items(item_list: ItemList):
    # Acessando os dados no JSON recebido
    if len(item_list.items) == 0:
        return {
            "message": "no item!"
        }
    
    for patient in item_list.items:
        patients = fila.Patient(patient.name, patient.age, patient.urgency)
        queue_patient.add_patient(patients)
    
    return {
        "message": "Itens!",
        "items": item_list.items,
        "display": queue_patient.display_queue(),
        "next": queue_patient.next_patient()
    }

if __name__ == '__main__':
    import uvicorn
    port = int(os.getenv("PORT"), 8000)
    uvicorn.run(app, host="127.0.0.1", port=port)