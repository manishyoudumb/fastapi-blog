from fastapi import FastAPI 
from datetime import datetime
from typing import List,Optional
from pydantic import BaseModel

app = FastAPI(
    title="Blog API",
    description="Blog API with FastAPI",
    version="0.0.1"
)
db = []
# Root endpoints here
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
    return db

@app.post("/posts", response_model=Post, status_code=201, tags=["Posts"])
def create_post(post: Post):
    db.append(post)
    return post

@app.get("/posts/{post_id}", response_model=Post, tags=["Posts"])
def get_post(post_id: int):
    
    try:
        return db[post_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Post not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))