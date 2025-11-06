from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"mensaje": "¡Hola desde FastAPI en macOS!"}