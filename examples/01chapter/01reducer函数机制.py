from tkinter import Image
from typing import Annotated,TypedDict,List
import operator
from langgraph.graph import START,StateGraph,END

def addition(state):

    msg = state["messages"][-1]
    response = {"x":msg["x"] + 1}
    print("response", state)
    return {"messages":[response]}


def subtraction(state):
    """subtraction"""
    msg = state['messages'][-1]
    response = {"x":msg["x"] - 2}
    print("state",state)
    return {"messages":[response]}

class State(TypedDict):
    messages:Annotated[List[str],operator.add]

builder = StateGraph(State)
builder.add_node("node1",addition)
builder.add_node("node2",subtraction)


# 构建边
builder.add_edge(START,"node1")
builder.add_edge("node1","node2")
builder.add_edge("node2",END)

graph = builder.compile()

from IPython.display import  display,Image
display(Image(graph.get_graph(xray=True).draw_mermaid()))
input_state = {"messages":[{"x":10}]}
graph.invoke(input_state)









