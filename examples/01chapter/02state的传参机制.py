from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import operator
from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, END
from IPython.display import display, Image
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI(
    model="gpt-4o",
    api_key="YOUR_OPENAI_API_KEY",
    base_url="https://koalaapi.com/v1",
    temperature=0.8,
)


class State(TypedDict):
    """定义图的状态模式"""
    messages: Annotated[List[str], operator.add]


# 创建图实例
builder = StateGraph(State)


def chat_with_model(state):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}


def convert_messages(state):
    # "您是一位数据提取专家,负责从文本中检索关键信息。请为所提供的文本提取相关信息,并以JSON格式输出、概述所提取的关键数据点。"
    EXTRACTIONPROMPT = """You are a data extraction specialist tasked with retrieving key information from a text.
      Extract such information for the provided textand output it in JSON format.Outline the key data points extracted."""

    messages = state['messages']
    messages = messages[-1]
    messages = [
        SystemMessage(content=EXTRACTIONPROMPT),
        HumanMessage(content=state["messages"][-1].content),
    ]
    response = llm.invoke(messages)
    return {"messages": [response]}


# 添加节点
builder.add_node("chat_with_model",chat_with_model)
builder.add_node("convert_messages",convert_messages)

# 设置启动节点
builder.set_entry_point("chat_with_model")

# 添加边
builder.add_edge("chat_with_model","convert_messages")
builder.add_edge("convert_messages",END)

graph = builder.compile()

display(Image(graph.get_graph(xray=True).draw_mermaid()))

query = "你好，请你介绍一下你自已"

input_message = {"messages":[HumanMessage(content=query)]}

result = graph.invoke(input_message)
print(result)



