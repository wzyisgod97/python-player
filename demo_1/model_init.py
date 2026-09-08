import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
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
# messages=[
#   {"role":"system","content":"你是一名资深的网易手游阴阳师玩家"},
#   {"role":"user","content":"SP面气灵现在有什么用"}
# ]
messages=[SystemMessage(content="你是一名资深的网易手游阴阳师玩家"),
          HumanMessage(content="我现在PVE输出主力式神是阿修罗和SP大舅妈,刚抽到雪御前、葛叶和SP紧那罗,我先培养哪个")
]
response1=deepseekClient.invoke(messages)
print(response1.content)
#添加记忆
# messages.append({"role":"assistant","content":response1.content})
messages.append(AIMessage(content=response1.content))
#新的提问
# messages.append( {"role":"user","content":"那SP清姬呢"})
messages.append(HumanMessage(content="如果想要打秘闻副本的话，该怎么培养"))
response2=deepseekClient.invoke(messages)
print(response2.content)
