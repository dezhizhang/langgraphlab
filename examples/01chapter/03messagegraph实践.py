import getpass
import operator
import os
from typing import TypedDict,List,Annotated

from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages

llm = ChatOpenAI(
    model="gpt-4o",
    api_key="YOUR_OPENAI_API_KEY",
    base_url="https://koalaapi.com/v1",
    temperature=0.8,
)


def chatbot(state):
    return {"messages": [llm.invoke(state["messages"])]}


from langgraph.graph.message import StateGraph

class State(TypedDict):
    messages: Annotated[list[str],add_messages]


builder = StateGraph(State)
builder.add_node("chatbot", lambda state: [("assistant", "你好，最帅气的人！")])
builder.set_entry_point("chatbot")
builder.set_finish_point("chatbot")

graph = builder.compile()
result = graph.invoke(["user"])
print(result)


