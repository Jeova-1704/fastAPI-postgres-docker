from pydantic import BaseModel


class ToDoBase(BaseModel):
    title: str
    description: str

class ToDoCreate(ToDoBase):
    pass

class ToDo(ToDoBase):
    id: int
    is_completed: bool
    user_id: int
    class Config:
        orm_mode = True