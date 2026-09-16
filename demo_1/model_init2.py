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
#消息字典调用
messages=[
  {"role":"system","content":"你是一名资深的网易手游阴阳师玩家"},
  {"role":"user","content":"SP面气灵现在有什么用"}
]
response1=model.invoke(messages)
print(response1.content)
#添加记忆
messages.append({"role":"assistant","content":response1.content})
#新的提问
messages.append( {"role":"user","content":"那SP清姬呢"})
response2=model.invoke(messages)
print(response2.content)