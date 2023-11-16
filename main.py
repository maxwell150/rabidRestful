"""module for running the application"""

from fastapi import FastAPI
import pymysql
from .db import engine
from . import models
from .routes import user, post, auth
from .db_config import password, database_name,user, host

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

try:
    con = pymysql.connect(host=host, user=user,passwd=password, database=database_name)
    cur = con.cursor()
    print("Database connection was successfull")
except Exception as err:
    print("Database connnection failed")
    print("error: ", err)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def login_user():
    return {"message": "You have Successfully logged in"}
