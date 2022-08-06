from fastapi import APIRouter,Request
from sqlalchemy.orm import Session 
from typing import List
from fastapi import Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import schemas
from fastapi.encoders import jsonable_encoder
import models
from database import connect_db
from utils import hash_pass
from flask import Flask
from fastapi.middleware.wsgi import WSGIMiddleware
app=Flask(__name__)
router=APIRouter()

# router.mount('/blog',WSGIMiddleware(app))

templates=Jinja2Templates(directory="templates")


@router.get("/user")
def get_users(request: Request,db:Session=Depends(connect_db)):

    data=db.query(models.User).all()
    data=jsonable_encoder(data)
    return data

    # # print(data.__dict__)
    # return templates.TemplateResponse("index.html",{"request":request ,"name":name,"data":data})
    



@router.get("/user/{id}")
def read_user(id:int,response:HTMLResponse,db:Session=Depends(connect_db)):
    data=db.query(models.User).filter(models.User.id==id).first()
    if data !=None:
        return f'<h1>{jsonable_encoder(data)}</h1>'
    else:
        return f"User with ID-{id} not found."    
    

@router.post("/create_user")
def create_user(user:schemas.UserCreate,db:Session=Depends(connect_db)):
    secure_password=hash_pass(user.password)
    
    #print(len(secure_password))
    user.password=secure_password
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id":new_user.id,"email":new_user.email}

@router.put("/update_user/{id}")
def update_user(user:schemas.UserCreate,id:int,db:Session=Depends(connect_db)):
    secure_password=hash_pass(user.password)
    pre_update_user=db.query(models.User).filter(models.User.id==id).first()
    pre_update_user.email=user.email
    pre_update_user.password=secure_password
    db.add(pre_update_user)
    db.commit()
    return {"message":f"Data Updated for user with New Email:{pre_update_user.email}"}

@router.delete("/delete_user/{id}")
def delete_user(id:int,db:Session=Depends(connect_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    print(user)
    db.delete(user)
    db.commit()


