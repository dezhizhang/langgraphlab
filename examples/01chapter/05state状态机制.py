
from typing import TypedDict
from langgraph.graph import START,StateGraph,END

class State(TypedDict):
    x:int
    y:int

def addition(state):
    print(state)
    return {"x":state['x'] + 1}

def subtraction(state):
    print(state)
    return {"x":state['x'] - 1}

# 构建图
builder = StateGraph()


# 向图中添加两个节点
builder.add_node("addition",addition)
builder.add_node("subtraction",subtraction)

# 构建节点之间的边
builder.add_edge(START,"addition")
builder.add_edge("addition","subtraction")
builder.add_edge("subtraction",END)


graph = builder.compile()


# 定义一个初始化状态
initial_state = {"x":10}

result = graph.invoke(initial_state)

png_bytes = graph.get_graph(xray=True).draw_mermaid_png()
with open("graph.png","wb") as f:
    f.write(png_bytes)

print("已保存为 graph.png")









#