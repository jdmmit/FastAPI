from fastapi import FastAPI

app = FastAPI()

# Iniciar el server uvicorn main:app --reload
                #   fastapi dev main.py


@app.get("/")
async def root():
    return "Hello, World!"

@app.get("/url_curso")
async def root():
    return {"url_curso":"https://mouredev.com/curso-fastapi-gratis"}
