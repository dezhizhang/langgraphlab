

from langchain_openai import ChatOpenAI
from typing import Annotated,TypedDict
from langgraph.graph import StateGraph,START,END




from typing import Annotated


# from typing import Annotated,TypedDict
# from langgraph.graph import StateGraph,START,END
# from langgraph.graph.message import add_messages
#
#
# class State(TypedDict):
#     messages: Annotated[list,add_messages]
#
# graph_builder = StateGraph(State)

# def chatbot(state:State):
#     print("state",state)
#     return {"messages":[llm.invoke(state["messages"])]}
#
# graph_builder.add_node("chatbot",chatbot)
#
# graph_builder.add_edge(START,"chatbot")
# graph_builder.add_edge("chatbot",END)
#
# graph = graph_builder.compile()
#
# def stream_graph_update(user_input:str):
#     for event in graph.stream({"messages":[("user",user_input)]}):
#         for value in event.values():
#             print("模型回复:",value["messages"][-1].content)
#
# while True:
#     try:
#         user_input = input("用户提问")
#         if user_input.lower() in ['退出']:
#             break
#
#         stream_graph_update(user_input)
#     except:
#         user_input = "what do you want to do?"
#         stream_graph_update(user_input)
#         break





