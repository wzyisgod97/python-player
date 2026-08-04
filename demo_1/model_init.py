import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
load_dotenv(override=True)
dsApiKey=os.getenv("ds_key")
dsApiUrl=os.getenv("ds_url")
deepseekClient=ChatDeepSeek(
     model="deepseek-v4-flash",
     api_key=dsApiKey,
     base_url=dsApiUrl
)
response=deepseekClient.invoke("你是谁")
print(response)