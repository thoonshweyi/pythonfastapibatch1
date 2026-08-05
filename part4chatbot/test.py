import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url="https://api.siliconflow.cn/v1",
)

try:
    models = client.models.list()
    print(models)
except Exception as e:
    print(type(e).__name__)
    print(e)