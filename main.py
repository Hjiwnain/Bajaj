from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class DataType(BaseModel):
    Name: str
    Email: str
    College: str
    StudentId: str
    FileName: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/bajaj_Test")
def main(dt: DataType):
    if(dt.Name is not None and dt.FileName is not None and dt.Email is not None and dt.College is not None and dt.StudentId is not None):
        return {"Message": "Received Your Data","Status": 200}
