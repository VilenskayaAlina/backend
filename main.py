from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Data(BaseModel):
    data: str

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Позволяет запросы с любых источников (для разработки, в продакшене лучше указать точный URL фронтенда)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP-методы
    allow_headers=["*"],  # Разрешить любые заголовки
)

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

@app.get("/api/get-data")
async def get_data():
    with open("data.txt", "r") as file:
        content = file.read()
    return {"data": content}