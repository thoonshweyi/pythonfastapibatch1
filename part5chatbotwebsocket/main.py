print("Hello, FastAPI with OpenAI API! This is the main.py file for the chatbot application.")
from openai import OpenAI
from fastapi import FastAPI, Form, Request, WebSocket
from typing import Annotated

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import os
from dotenv import load_dotenv

from huggingface_hub import InferenceClient
import uuid
from pathlib import Path

load_dotenv()

app = FastAPI()
client = OpenAI(
     api_key=os.getenv("HUGGING_FACE_API_KEY"),
     base_url="https://router.huggingface.co/v1"   
)
imageClient = InferenceClient(
     api_key=os.getenv("HUGGING_FACE_API_KEY"),
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

# => Test Generate (Before websocket)
# @app.post('/',response_class=HTMLResponse)
# async def chat(request:Request,userinput:Annotated[str,Form()]):
     
#      chatlogs.append({"role": "user","content":userinput})

#      datas.append(userinput)

#      completion = client.chat.completions.create(
#           model="gemma4:31b-cloud", # openrouter.ai changes
#           store=False,
#           messages=chatlogs,
#           temperature= 0.6 # .5 (0 to 2)
#      )

#      botresponse = completion.choices[0].message.content
#      chatlogs.append({"role": "assistant","content":botresponse})
    
#      datas.append(botresponse)
     
#      return templates.TemplateResponse(
          
#           request= request,name = "layout.html",context={"datas":datas}
#           # 'layout.html',{"request":request,"datas":datas}

#      )

# => Text Generate (After websocket, without streaming)
# exe 1
# @app.websocket("/ws")
# async def chat(websocket: WebSocket):
#      await websocket.accept()
#      while True:
#           userinput = await websocket.receive_text()
#           await websocket.send_text(f"Message text was: {userinput}")

# exe 2
# @app.websocket("/ws")
# async def chat(websocket: WebSocket):
#      await websocket.accept()
#      while True:
#           userinput = await websocket.receive_text()
          
#           chatlogs.append({"role": "user","content":userinput})          
     
#           try: 
#                completion = client.chat.completions.create(
#                     model="gemma4:31b-cloud",
#                     store=False,
#                     messages=chatlogs,
#                     temperature= 0.6 # .5 (0 to 2)
#                )

#                botresponse = completion.choices[0].message.content
#                # await websocket.send_text(str(completion))
#                await websocket.send_text(botresponse)
               
#                chatlogs.append({"role": "assistant","content":botresponse})          
               
                    
#           except Exception as err:
#                await websocket.send_text(f"Error Found: {str(err)}")
#                break;


# => Text Generate (After websocket, with streaming)
@app.websocket("/ws")
async def chat(websocket: WebSocket):
     await websocket.accept()
     while True:
          userinput = await websocket.receive_text()
          
          chatlogs.append({"role": "user","content":userinput})          
     
          try: 
               completion = client.chat.completions.create(
                    model="deepseek-ai/DeepSeek-V4-Flash-0731:novita",
                    store=False,
                    messages=chatlogs,
                    temperature= 0.6, # .5 (0 to 2)
                    stream=True
               )

               for chunk in completion:
                    botresponse = chunk.choices[0].delta.content
                    # await websocket.send_text(str(chunk))
                    
                    if botresponse is not None:
                         await websocket.send_text(str(botresponse))
                         # chatlogs.append({"role": "assistant","content":botresponse})          
                    
                    
          except Exception as err:
               await websocket.send_text(f"Error Found: {str(err)}")
               break;
               
# result (without streaming)               
# ChatCompletion(id='chatcmpl-358', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='*Adjusts colorful collar and leans in with a mischievous grin*\n\n**"Haaa-haaa! You want a joke about web development? I’ve got a real *classic* for you!"**\n\n***\n\n**Why did the web developer walk out of the restaurant?**\n\n**Because the table layout was `float: left` and he couldn\'t find the `clear`!**\n\n***\n\n*Cackles loudly* \n\n**"Get it? Get it?! Now go back to your CSS and try to center a Div for three hours! HAHAHA!"**', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None))], created=1785515263, model='gemma4:31b', object='chat.completion', moderation=None, service_tier=None, system_fingerprint='fp_ollama', usage=CompletionUsage(completion_tokens=123, prompt_tokens=31, total_tokens=154, completion_tokens_details=None, prompt_tokens_details=None))
         
# result (streaming)
# ChatCompletionChunk(id='chatcmpl-678', choices=[Choice(delta=ChoiceDelta(content='*! HAHAHA!"', function_call=None, refusal=None, role='assistant', tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1785514941, model='gemma4:31b', object='chat.completion.chunk', moderation=None, service_tier=None, system_fingerprint='fp_ollama', usage=None)

# Image Generate
@app.get("/image", response_class=HTMLResponse)
async def image(request: Request):
     return templates.TemplateResponse(
        request=request,
        name="image.html",
        context={
            "data": None,
            "error": None,
        },
     )

# => Image Generate (Before websocket)
# @app.post('/image',response_class=HTMLResponse)
# async def generateimage(request:Request,userinput:Annotated[str,Form()]):
     
#      error = None
#      data = None

#      try:
#           # completion = client.images.generate(
#           #      model="dall-e-2",
#           #      prompt= userinput,
#           #      size="256x256",
#           #      # quality="standard",
#           #      n=1,
#           # )

#           # botresponse = completion.data[0].url
    
#           # if not completion.data or not botresponse:
#           #       raise ValueError("No image generated")
     
#           # update data to the template
#           botresponse = "image"
#           return templates.TemplateResponse(
#                # request= request,name = "image.html",context={"data":botresponse}
#                'image.html',{"request":request,"data":botresponse,"error":error}
#           )
#      except Exception as e:
#               return templates.TemplateResponse(
#                     'image.html',{"request":request,"data":data, "error": f"Error generating image: {str(e)}"}
#                )
     
# => Image Generate (After websocket)
# @app.websocket("/image")
# async def generateimage(websocket: WebSocket):
#      await websocket.accept()
#      while True:
#           userinput = await websocket.receive_text()
     
#           try: 
#                completion = client.images.generate(
#                     model="dall-e-2",
#                     prompt= userinput,
#                     size="256x256",
#                     n=1,
#                )

#                botresponse = completion.data[0].url
        
#                if not completion.data or not botresponse:
#                     raise ValueError("No image generated")
               
#                await websocket.send_text(str(botresponse))
               
#           except Exception as err:
#                await websocket.send_text(f"Error Found: {str(err)}")
#                break;
               
    
# =>by huggingface
@app.websocket("/image")
async def generateimage(websocket: WebSocket):
     
     await websocket.accept()
     while True:
          userinput = await websocket.receive_text()
     
          try: 
               botresponse = generate_image(
                    imageClient=imageClient,
                    prompt=userinput,
                    model="black-forest-labs/FLUX.1-schnell",  # သို့မဟုတ် "stabilityai/stable-diffusion-xl-base-1.0"
                    size="1024x1024",
                    n=1
               )

               if not botresponse:
                    raise ValueError("No image generated")

               await websocket.send_text(str(botresponse))
               
          except Exception as err:
               await websocket.send_text(f"Error Found: {str(err)}")
               break;
 
     
              
def generate_image(
    imageClient: InferenceClient,
    prompt: str,
    model: str = "black-forest-labs/FLUX.1-schnell",
    size: str = "1024x1024",
    n: int = 1
) -> Optional[str]:
     try:
          try:
               width, height = map(int, size.split("x"))
          except ValueError:
               width, height = 1024, 1024

          image = imageClient.text_to_image(
               prompt=prompt,
               model=model,
               width=width,
               height=height
          )

          # Unique file name ဖြင့် Save ခြင်း
          OUTPUT_DIR = Path("static/generated_images")
          OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
          
          filename = f"{uuid.uuid4()}.png"
          file_path = OUTPUT_DIR / filename
          image.save(file_path)

          return f"/static/generated_images/{filename}"

     except Exception as e:
          print("Error in generate_image:", e)
          return None

# uvicorn main:app --reload

