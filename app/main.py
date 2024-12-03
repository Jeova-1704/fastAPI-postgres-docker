from fastapi import FastAPI
from app.api import auth, todo
from app.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(todo.router, prefix="/todos", tags=["To-Do"])
