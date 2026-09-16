import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from rich import print as rich_print
load_dotenv(override=True)
dsApiKey=os.getenv("ds_key")
dsApiUrl=os.getenv("ds_url")
chatModel=init_chat_model(
     model="deepseek-v4-flash",
     api_key=dsApiKey,
     base_url=dsApiUrl
)
messages=[SystemMessage(content="你是一名资深的网易手游阴阳师玩家"),
          HumanMessage(content="我现在PVE输出主力式神是阿修罗和SP大舅妈,刚抽到雪御前、葛叶和SP紧那罗,我先培养哪个")
]
response1=chatModel.invoke(messages)
print(response1.content)
#添加记忆
messages.append(AIMessage(content=response1.content))
#新的提问
messages.append(HumanMessage(content="如果想要打秘闻副本的话，该怎么培养"))
response2=chatModel.invoke(messages)
print(response2.content)
#美化输出内容1
response2.pretty_repr
#美化输出内容 使用rich库
rich_print(response2)