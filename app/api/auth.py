from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, Token
from app.services.auth import create_user, authenticate_user, create_token
from app.database.connection import get_db

router = APIRouter()

@router.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(username=user.username, password=user.password, db=db)
    return create_token(new_user)

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(username=user.username, password=user.password, db=db)
    return create_token(authenticated_user)
