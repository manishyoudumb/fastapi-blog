from fastapi import FastAPI 
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

app = FastAPI(
    title="Blog API",
    description="Blog API with FastAPI",
    version="0.0.1"
)

@app.get("/", tags=["Root"])
def read_root():
    return {"Welcome to Blog-API"}


class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    created_on:datetime=datetime.now()

    @app.get("/posts", tags=["Posts"])
    def get_posts():
        return {"data": "There will be a list of posts"}