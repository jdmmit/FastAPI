from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciar el server uvicorn users:app --reload
                #   fastapi dev users.py

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Brais", surname="Moure", url="https://mouredev.com", age=36), User(id=2, name="John", surname="Doe", url="https://johndoe.com", age=30), User(id=3, name="Pablo", surname="peladonerd", url="https://peladonerd.com", age=28)]

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

# Path parameters
@app.get("/user/{id}")
async def get_user_by_path(id: int):
    return search_user(id)

# Query parameters
@app.get("/user/")
async def get_user_by_query(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}