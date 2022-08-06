from click import password_option
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    #id:int
    email:EmailStr
    password:str
class UserOut(BaseModel):
    id: int
    email: EmailStr
    # created_at: datetime

    class Config:
        orm_mode = True