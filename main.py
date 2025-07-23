from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, World!"

@app.get("/url_curso")
async def root():
    return {"url_curso":"https://mouredev.com/curso-fastapi-gratis"}