from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}   
@app.get('/World/1')
def read_about():
    return {"Hello": 1}