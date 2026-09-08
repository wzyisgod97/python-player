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
# response=deepseekClient.invoke("你是谁")
# print(response)
#消息字典调用
messages=[
  {"role":"system","content":"你是一名资深的网易手游阴阳师玩家"},
  {"role":"user","content":"SP面气灵现在有什么用"}
]
response1=deepseekClient.invoke(messages)
print(response1)
#添加记忆
messages.append({"role":"assistant","content":response1.content})
#新的提问
messages.append( {"role":"user","content":"那SP清姬呢"})
response2=deepseekClient.invoke(messages)
print(response2)
