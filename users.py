from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciar el server uvicorn users:app --reload
                #   fastapi dev users.py

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Brais", surname="Moure", url="https://mouredev.com", age=36), User(name="John", surname="Doe", url="https://johndoe.com", age=30), User(name="Pablo", surname="peladonerd", url="https://peladonerd.com", age=28)]

@app.get("/usersjson")
async def usersjson():
    return [
        {"name": "Brais", "surname": "Moure", "url": "https://mouredev.com", "age": 36},
        {"name": "John", "surname": "Doe", "url": "https://johndoe.com", "age": 30},
        {"name": "Pablo", "suername": "peladonerd", "url": "https://peladonerd.com", "age": 28}
        ]

@app.get("/users")
async def users():
    return users_list