from sqlalchemy.orm import Session
from typing import List, Dict
from fastapi import Depends, status, HTTPException, APIRouter
from ..db import engine, get_db
from .. import models, schemas, utils

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED)#response_model=schemas.UserOut gives error
def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    # hashing the password
    user.password = utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    return db.refresh(new_user)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def find_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')