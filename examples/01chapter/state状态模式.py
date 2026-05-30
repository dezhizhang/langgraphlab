

from langgraph.graph import StateGraph
from typing import Dict

# 构建图
builder = StateGraph(dict)

def addition(state):
    print(state)
    return {"x":state["x"] + 1}

def subtraction(state):
    print(state)
    return {"y":state["x"] - 2}

from langgraph.graph import START,END

# 添加节点
builder.add_node("addition",addition)
builder.add_node("subtraction",subtraction)

# 构建节点之间的边
builder.add_edge(START,"addition")
builder.add_edge("addition","subtraction")
builder.add_edge("subtraction",END)

graph = builder.compile()




