from sqlalchemy.orm import Session
from app.database.models import ToDo
from app.schemas.Todo import ToDoCreate
from fastapi import HTTPException

def create_todo(todo: ToDoCreate, user_id: int, db: Session):
    new_todo = ToDo(**todo.dict(), user_id=user_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def get_todos(user_id: int, db: Session):
    return db.query(ToDo).filter(ToDo.user_id == user_id).all()

def get_todo_by_id(todo_id: int, user_id: int, db: Session):
    todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.user_id == user_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do not found")
    return todo

def update_todo(todo_id: int, user_id: int, todo_data: ToDoCreate, db: Session):
    todo = get_todo_by_id(todo_id, user_id, db)
    todo.title = todo_data.title
    todo.description = todo_data.description
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(todo_id: int, user_id: int, db: Session):
    todo = get_todo_by_id(todo_id, user_id, db)
    db.delete(todo)
    db.commit()
    return {"detail": "To-Do deleted successfully"}
