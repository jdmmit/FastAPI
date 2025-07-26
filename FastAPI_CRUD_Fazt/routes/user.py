from fastapi import APIRouter

user = APIRouter()

@user.get("/")
def helloworld():
    return {"message": "Hello World from User Route"}