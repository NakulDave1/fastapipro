from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


MYSQL_URL='mysql+pymysql://root:hpsystem@localhost/fastapi'


engine=create_engine(MYSQL_URL) #this creaate engine will establish connection with the database 

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) #and this will help in making sessional connection with database 

Base =declarative_base()

def connect_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()    