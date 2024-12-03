from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.Todo import ToDo, ToDoCreate
from app.services.todo import create_todo, get_todos, update_todo, delete_todo
from app.database.connection import get_db
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=ToDo)
def create_todo_route(todo: ToDoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    print(todo)
    print(db)
    print(user)
    return create_todo(todo, user.id, db)

@router.get("/", response_model=List[ToDo])
def get_todos_route(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_todos(user.id, db)

@router.put("/{todo_id}", response_model=ToDo)
def update_todo_route(todo_id: int, todo: ToDoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return update_todo(todo_id, user.id, todo, db)

@router.delete("/{todo_id}")
def delete_todo_route(todo_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return delete_todo(todo_id, user.id, db)
