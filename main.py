from fastapi import FastAPI
from pydantic import BaseModel


class mail(BaseModel):
    subject: str
    text: str
    test: int

app = FastAPI()

def fun(x):
    return x+1

@app.post("/items/")
async def create_item(mail: mail):
    value =  fun(mail.test)
    return value
