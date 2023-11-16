from sqlalchemy.orm import Session
from typing import List, Dict
from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy import desc
from ..db import engine, get_db
from .. import models, schemas, oauth2

router = APIRouter(
    prefix= "/posts",
    tags=['Posts']
)

@router.get('/', response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return  posts

@router.post('/create_post', status_code=status.HTTP_201_CREATED) #response_model=schemas.Post) gives error
def create_post(data: schemas.postTemplate, db: Session=Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):

    print(current_user.id)
    # post = models.Post(**data.model_dump())
    print('------------------------------------')
    data = data.model_dump()
    data.update({'user_id': current_user.id})
    post = models.Post(**data)
    db.add(post)
    db.commit()


#GET
@router.get("/latest", response_model=schemas.Post)
def get_latest(db: Session=Depends(get_db)):
    post = db.query(models.Post).order_by(desc(models.Post.id)).first()
    return post


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Post with id {id} not found")
    return  post

#DELETE    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session=Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} not found")
    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, content: schemas.postTemplate, db: Session=Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} does not exist")
    
    post_query.update(content.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()





