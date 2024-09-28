from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    data: str

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Backend"}

@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon available"}

@app.post("/api/save-data")
async def save_data(item: Data):
    with open("data.txt", "a") as file:
        file.write(item.data + "\n")
    return {"message": "Data saved"}
