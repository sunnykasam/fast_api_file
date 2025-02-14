from sqlalchemy import Integer,String,Column,Boolean
from database1 import Base

class info(Base):
    __tablename__='data_info'

    id=Column(Integer,primary_key=True,index=True) 
    userName=Column(String(90))
    email=Column(String(90),unique=True)
    phone_no=Column(String(20),unique=True)