from sqlalchemy.orm import Session
from app.database.models import User
from app.core.security import verify_password, get_password_hash, create_access_token
from fastapi import HTTPException

def create_user(username:str, password:str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return user

def create_token(user: User):
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}