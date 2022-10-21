from fastapi import FastAPI,Query
from typing import Union,Optional,List



# FastAPI instance
app = FastAPI()


# Path Parameters

# http://127.0.0.1:8000/ 
# Path Operation Decorator
@app.get("/")
# Path Operation Function
def read_root():
    return {"Hello": "World"}


# http://127.0.0.1:8000/blogs
@app.get("/blogs")
def display_blogs():
    return {"data":{'blogs list'}}


# http://127.0.0.1:8000/blogs/unpublished
@app.get("/blogs/unpublished")
def display_unpublished_blogs():
    return {"Unpublished Blogs":{'List of unpublished blogs'}}




# Query Parameters

# http://127.0.0.1:8000/blogs/5
@app.get("/blogs/{b_id}")
def get_blog_with_id(b_id:int):
    return {"blog_id":b_id, "blog":"Blog Body"}


# http://127.0.0.1:8000/blogs/5/comments
@app.get("/blogs/{b_id}/comments")
def get_comments_blog_with_id(b_id:int):
    return {"blog_id":b_id, "blog":"Blog Body" ,"comments":{'comments list'}}


# http://127.0.0.1:8000/limit/?limit=50&published=false
# http://127.0.0.1:8000/limit/?limit=500&published=true
@app.get("/limit/")
def index(limit:Optional[int]=50, published:Optional[bool]=False):
    if published:
        return {"data":f'{limit} published blogs from the db'}
    else:
        return {"data":f'{limit} blogs from the db'}


# http://127.0.0.1:8000/items/5?q=5
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# http://127.0.0.1:8000/first/?que=5&opt=9
@app.get("/first/")
def index(que: int, opt: Optional[int] = 0):
    return {"Query = ": que, "Optional = ": opt}


# http://127.0.0.1:8000/first/abc/xyz
@app.get("/first/{file_path:path}")
def index(file_path: str):
    return {"File Path is = ": file_path}





"""

# Request Body
class User(BaseModel):
    user_id: int
    name: str
    password: str
    address: Optional[str] = None


@app.post("/users")
def index(user: User):
    return user


@app.post("/users/{user_id}")
def index(user: User, user_id: int):
    return user_id


# Query Parameters Validation
@app.get("/item")
def index(query: Optional[str] = Query(None, min_length=3, max_length=5, regex="^xxx")):
    return {query}


@app.get("/items")
def index(query1: Optional[List[str]] = Query(["foo", "bar"])):
    # Query(None)
    # Query([])
    return query1

"""
