from fastapi import FastAPI
from .routers import users
from .database import Base, engine

app = FastAPI(title="User Service (MySQL)")

# Crea las tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "User Service running with MySQL"}