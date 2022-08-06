from fastapi import FastAPI,Depends,APIRouter,Request
import models
from sqlalchemy.orm import Session
from database import engine,connect_db
from fastapi.encoders import jsonable_encoder
from router import user
from fastapi.middleware.wsgi import WSGIMiddleware

app=FastAPI()

app.include_router(user.router)
models.Base.metadata.create_all(bind=engine)
@app.get("/")
def check_point():
    return {"message":"API  has started successfully "}


