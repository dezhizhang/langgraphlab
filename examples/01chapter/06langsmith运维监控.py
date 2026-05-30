from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os


os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = "YOUR_LANGSMITH_API_KEY"
os.environ["LANGSMITH_PROJECT"] = "test"


from typing import Annotated,TypedDict
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list,add_messages]

graph_builder = StateGraph(State)

llm = ChatOpenAI(
    model="gpt-4o",
    api_key="YOUR_OPENAI_API_KEY",
    base_url="https://koalaapi.com/v1",
    temperature=0.8,
)

def chatbot(state:State):
    print("state",state)
    return {"messages":[llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot",chatbot)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)

graph = graph_builder.compile()

def stream_graph_update(user_input:str):
    for event in graph.stream({"messages":[("user",user_input)]}):
        for value in event.values():
            print("模型回复:",value["messages"][-1].content)

while True:
    try:
        user_input = input("用户提问")
        if user_input.lower() in ['退出']:
            break

        stream_graph_update(user_input)
    except:
        user_input = "what do you want to do?"
        stream_graph_update(user_input)
        break





