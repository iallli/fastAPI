
from fastapi import FastAPI, HTTPException, Query, Depends, status, Response

from typing import Union, Optional, List

from sqlalchemy.orm import Session

from models import Blog
from schemas import BlogSchema, get_db


# FastAPI instance
app = FastAPI()


# http://127.0.0.1:8000/
# Path Operation Decorator
@app.get("/")
# Path Operation Function
def read_root():
    return {"Hello": "World"}


"""
# Path Parameters

# http://127.0.0.1:8000/blogs
@app.get("/blogs")
def display_blogs():
    return {"data": {'blogs list'}}


# http://127.0.0.1:8000/blogs/unpublished
@app.get("/blogs/unpublished")
def display_unpublished_blogs():
    return {"Unpublished Blogs": {'List of unpublished blogs'}}


# Query Parameters

# http://127.0.0.1:8000/blogs/5
@app.get("/blogs/{b_id}")
def get_blog_with_id(b_id: int):
    return {"blog_id": b_id, "blog": "Blog Body"}


# http://127.0.0.1:8000/blogs/5/comments
@app.get("/blogs/{b_id}/comments")
def get_comments_blog_with_id(b_id: int):
    return {"blog_id": b_id, "blog": "Blog Body", "comments": {'comments list'}}


# http://127.0.0.1:8000/limit/?limit=50&published=false
# http://127.0.0.1:8000/limit/?limit=500&published=true
@app.get("/limit/")
def limit(limit: Optional[int] = 50, published: Optional[bool] = False):
    if published:
        return {"data": f'{limit} published blogs from the db'}
    else:
        return {"data": f'{limit} blogs from the db'}


# http://127.0.0.1:8000/items/5?q=5
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# http://127.0.0.1:8000/first/?que=5&opt=9
@app.get("/first/")
def first(que: int, opt: Optional[int] = 0):
    return {"Query = ": que, "Optional = ": opt}


# http://127.0.0.1:8000/first/abc/xyz
@app.get("/first/{file_path:path}")
def file_path(file_path: str):
    return {"File Path is = ": file_path}


# Query Parameters Validation
@app.get("/item")
def item(query: Optional[str] = Query(None, min_length=3, max_length=5, regex="^xxx")):
    return {query}


@app.get("/items")
def items(query1: Optional[List[str]] = Query(["foo", "bar"])):
    # Query(None)
    # Query([])
    return query1


# Uses of Dependency Injection

class CommonParam:
    def __init__(self, q: str, skip: int = 0, limit: int = 0):
        self.q = q
        self.skip = skip
        self.limit = limit


async def common_param(q: str, skip: Optional[int] = 9, limit: Optional[int] = 9):
    return {"Query = ": q, "Skip = ": skip, "Limit = ": limit}


@app.get("/depend")
async def read_items(commons: dict = Depends(common_param)):
    return commons


@app.get("/depend1")
async def read_users(commons: dict = Depends(common_param)):
    return commons


@app.get("/depend2")
async def read_all(commons: CommonParam = Depends(CommonParam)):
    return {commons.q + (str)(commons.skip) + (str)(commons.limit)}

"""


#   sqlalchemy supports ORM = Object Relationship Mapping

# Post data into DB
@app.post("/blogs", status_code=status.HTTP_201_CREATED, response_model=BlogSchema)
def post_blogs(user: BlogSchema, db: Session = Depends(get_db)):
    u = Blog(id=user.id, title=user.title, body=user.body)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

# Get data from DB


@app.get("/blogs", status_code=200, response_model=List[BlogSchema])
def get_blogs(response: Response, db: Session = Depends(get_db)):
    return db.query(Blog).all()


@app.get("/blogs/{b_id}", status_code=200, response_model=BlogSchema)
def get_blogs(b_id, response: Response, db: Session = Depends(get_db)):
    us = db.query(Blog).filter(Blog.id == b_id).first()
    if not us:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id={b_id} not found.")
    return us


@app.delete("/blogs/{b_id1}")
def delete_blog(b_id1: int, db: Session = Depends(get_db)):
    us1 = db.query(Blog).filter(Blog.id == b_id1).delete(
        synchronize_session=False)
    db.commit()
    if not us1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id={b_id1} not found.")
    return us1
