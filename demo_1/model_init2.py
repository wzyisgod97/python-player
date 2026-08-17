from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv(override=True)

DS_KEY=os.getenv("ds_key")
DS_URL=os.getenv("ds_url")
DS_MODEL=os.getenv("ds_model")
##使用统一封装的接口init_chat_model进行调用
model=init_chat_model(
    model=DS_MODEL,
    api_key=DS_KEY,
    base_url=DS_URL
    )
result=model.invoke("你是谁")
print(result)