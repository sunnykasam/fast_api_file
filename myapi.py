from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
import table_data
from database1 import engine,sessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

table_data.Base.metadata.create_all(bind=engine)

class About(BaseModel):
    id:int
    userName:str
    email:str
    phone_no:str


def get_data():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_data)]


@app.get("/")
def read_root():
    return {"Hello": "World"}  



@app.post('/about')
def  read_item(user:About,db:db_dependency):
    db_post=table_data.info(**user.dict())
    db.add(db_post)
    db.commit()



@app.get('/about/{user_id}',status_code=status.HTTP_200_OK)
def  read_item(user_id:int, db:db_dependency):
    user=db.query(table_data.info).filter(table_data.info.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user
    #return {"information": "This is a information page"}




@app.delete('/about/delete/{id}',status_code=status.HTTP_200_OK)
def read_about(id: int,db:db_dependency):
    db_delete=db.query(table_data.info).filter(table_data.info.id==id).first()
    if  db_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    db.delete(db_delete)
    db.commit()



#@app.get('/about/{id}/comments')
#def read_comments(id):
    #return {"data":{"1","2"}}