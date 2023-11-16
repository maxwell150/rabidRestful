from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import db, models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(user_data: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(db.get_db)):
    user = db.query(models.User).filter(models.User.email == user_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')
    if not utils.pswd_context.verify(user_data.password, user.password):
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"acess_token":access_token, "token_type": "Bearer"}  


    

