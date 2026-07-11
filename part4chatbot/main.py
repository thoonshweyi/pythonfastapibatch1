from openai import OpenAI
from fastapi import FastAPI, Form, Request, WebSocket
from typing import Annotated

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
client = OpenAI(
     api_key = os.getenv('OPEN_API_KEY')
)

templates = Jinja2Templates(directory="templates")

# Mount static directory
app.mount('/static',StaticFiles(directory='static'),name="static")


# => Chat Log and Keep History
# chatlogs = []
chatlogs = [{
     "role": "system",
     "content": "You are a joker.\
          Tell the joke for web development" #mean next new line
}]
datas = []


# => Template 
@app.get('/',response_class=HTMLResponse)
async def chatpage(request:Request):
     return templates.TemplateResponse(
          # request= request,name = "layout.html"
          # 'layout.html',{"request":request}

          request= request,name = "layout.html",context={"datas":datas}
          # 'layout.html',{"request":request,"datas":datas}

     )


@app.post('/',response_class=HTMLResponse)
async def chat(request:Request,userinput:Annotated[str,Form()]):
     
     chatlogs.append({"role": "user","content":userinput})

     datas.append(userinput)

     completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          store=False,
          messages=chatlogs,
          temperature= 0.6 # .5 (0 to 2)
     )

     botresponse = completion.choices[0].message.content
     chatlogs.append({"role": "assistant","content":botresponse})
    
     datas.append(botresponse)
     
     return templates.TemplateResponse(
          
          request= request,name = "layout.html",context={"datas":datas}

          # 'layout.html',{"request":request,"datas":datas}

     )


@app.get('/image',response_class=HTMLResponse)
async def image(request:Request):
     return templates.TemplateResponse(
          # request=request,name="image.html"
          "image.html",{"request":request,"data":None,"error":None}
     )

@app.post('/image',response_class=HTMLResponse)
async def generateimage(request:Request,userinput:Annotated[str,Form()]):
     
     error = None
     data = None

     try:
          completion = client.images.generate(
               model="dall-e-2",
               prompt= userinput,
               size="256x256",
               # quality="standard",
               n=1,
          )

          botresponse = completion.data[0].url
    
          if not completion.data or not botresponse:
                raise ValueError("No image generated")
     
          # update data to the template
          return templates.TemplateResponse(
               # request= request,name = "image.html",context={"data":botresponse}
               'image.html',{"request":request,"data":botresponse,"error":error}
          )
     except Exception as e:
              return templates.TemplateResponse(
                    'image.html',{"request":request,"data":data, "error": f"Error generating image: {str(e)}"}
               )
     
    


# uvicorn main:app --reload


# https://fastapi.tiangolo.com/reference/templating/
# https://fastapi.tiangolo.com/advanced/custom-response/#html-response

# template example
# https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates




# Why use Annotated here?
# Because you're using FastAPI!

# FastAPI needs to know where to get userinput from (from the form body, not from query parameters or JSON body).

# By using Form(), you tell FastAPI: “Hey, expect this userinput inside a form submission (application/x-www-form-urlencoded or multipart/form-data).”

# Without Annotated and Form(), FastAPI would not know how to parse the incoming form field properly.

# Annotated is a way to attach extra information (hints) to a normal Python type without changing how the type works.
#  Annotated = real type + extra information for tools/frameworks


# ① Browser sends request to FastAPI
# User opens the page http://localhost:8000/

# FastAPI receives the request.


# ② FastAPI calls your function chatpage
# FastAPI sees that / is handled by chatpage.

# So FastAPI calls your chatpage() function.

# ③ Inside chatpage(), you tell FastAPI:
# Load the file templates/layout.html

# Render it (fill in any data if needed)

# Return the result as a TemplateResponse

# ④ What happens inside TemplateResponse?
# 🔵 FastAPI uses Jinja2, a template engine.

# 🔵 Steps:

# Find the file templates/layout.html

# Read the file → (it’s just text with some Jinja tags like {{ }}, {% %}).

# Render it → Jinja2 fills in any placeholders (like replacing {{ username }} with "John", etc).

# Create a full HTML string.


# ⑤ FastAPI wraps the HTML into HTMLResponse
# The rendered HTML string is given to HTMLResponse.

# HTMLResponse prepares a proper HTTP response:

# Content-Type header = text/html

# Status Code = 200 OK

# Body = your full HTML page

# ✅ Now it’s ready to send back to the browser.

# ⑥ FastAPI sends the response to the browser
# The browser receives the HTTP response.

# The browser reads the HTML.

# The browser displays the web page!



# 🔵 Why Jinja2 Template needs request?
# ✅ Because FastAPI's TemplateResponse depends on request for some features.

# Even though pure Jinja2 (without FastAPI) doesn't need request,
# FastAPI needs it for special things.

# 🔥 Main Reasons:

# Why	Explanation
# 1. URL building	Inside template, you can use url_for() to build links dynamically. url_for() needs request.
# 2. Security	Some authentication (user session, cookies) information is inside request.
# 3. Internal FastAPI system	FastAPI's response generation uses request to build proper headers and background tasks if needed.



# 5WS