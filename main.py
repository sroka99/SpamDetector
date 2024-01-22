from fastapi import FastAPI
from pydantic import BaseModel
import functions as fun
import function1 as fun1

class mail(BaseModel):
            sender: str
            content: str

app = FastAPI()

@app.post("/items/")
async def create_item(mail: mail):
    fun.dodaj_mail(mail.sender,mail.content)
    return fun1.mail_check([mail.content])
