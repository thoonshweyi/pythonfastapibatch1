from fastapi import FastAPI

app = FastAPI()

# => get() , GET method does not have Body datas
@app.get('/')
async def greet():
     return {"message":"Hello World"}


@app.get('/about')
async def about():
     return {"message":"Hello I am about page."}

POSTS = [
     {"id":1,"title":"This is new post 1","category":"news","user_id":1},
     {"id":2,"title":"This is new post 2","category":"sport","user_id":1},
     {"id":3,"title":"This is new post 3","category":"news","user_id":1},
     {"id":4,"title":"This is new post 4","category":"health","user_id":1},
     {"id":5,"title":"This is new post 5","category":"news","user_id":1},
     {"id":6,"title":"This is new post 6","category":"sport","user_id":1},
     {"id":7,"title":"This is new post 7","category":"news","user_id":2},
     {"id":8,"title":"This is new post 8","category":"education","user_id":2},
     {"id":9,"title":"This is new post 9","category":"news","user_id":2},
     {"id":10,"title":"This is new post 10","category":"education","user_id":2},

]


@app.get('/posts')
async def allposts():
     return POSTS

# => Path Parameters (single data)
@app.get('/posts/intro')
async def intropost():
     return {"message":"This is post introdution"}

# @app.get('/posts/{dynamicparam}')
# async def getparam(dynamicparam:str):
#      return {"dynamic param": dynamicparam}


# method 1
# @app.get('/posts/{category}')
# async def getpostsbycategory(category:str):
#           for post in POSTS:
#                if post['category'].casefold() == category.casefold():
#                     return post

# method 2
# @app.get('/posts/{category}')
# async def getpostsbycategory(category:str):
#           for post in POSTS:
#                if post.get('category').casefold() == category.casefold():
#                     return post


# @app.get('/posts/title/{title}')
# @app.get('/posts/{title}')
# async def getpostsbytitle(title:str):
#           for post in POSTS:
#                if post.get('title').casefold() == title.casefold():
#                     return post




# => Query Parameters (multi data)  ?category=xxxx

# method 1
# @app.get('/posts/{userid}/')
# async def getusercategorybyquery(userid:int,category:str):
#      datas = []
#      for post in POSTS:
#           if post.get('user_id') == userid:
#                if post.get('category').casefold() == category.casefold():
#                     datas.append(post)
#      return  datas

# method 2
# @app.get('/posts/{userid}/')
# async def getusercategorybyquery(userid:int,category:str):
#      datas = []
#      for post in POSTS:
#           if post.get("user_id") == userid and post.get('category').casefold() == category.casefold():
#                datas.append(post)
#      return  datas

# method 3
# @app.get('/posts/{userid}/')
# async def getusercategorybyquery(userid:int,category:str):
#      datas = []
#      for post in POSTS:
#           if (post.get("user_id") == userid 
#           and post.get('category').casefold() == category.casefold()):
#                datas.append(post)
#      return  datas


# method 4
# @app.get('/posts/{userid}/')
# async def getusercategorybyquery(userid:int,category:str):
#      datas = []
#      for post in POSTS:
#           if post.get("user_id") == userid \
#           and post.get('category').casefold() == category.casefold():
#                datas.append(post)
#      return  datas


#   uvicorn post:app --reload



