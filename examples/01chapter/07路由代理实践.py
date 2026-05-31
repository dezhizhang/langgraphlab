from langgraph.graph import START, StateGraph, END
from typing import Annotated, TypedDict


class State(TypedDict):
    x: int


def node_a(state: State):
    return {"x": state['x'] + 1}


def node_b(state: State):
    return {"x": state['x'] - 2}


def node_c(state: State):
    return {"x": state['x'] + 1}

def routing_function(state:State):
    if state['x'] == 10:
        return "node_b"
    else:
        return "node_c"


builder = StateGraph(State)
builder.add_node("node_a",node_a)
builder.add_node("node_b",node_b)
builder.add_node("node_c",node_c)


builder.set_entry_point("node_a")
builder.add_conditional_edges("node_a",routing_function,["node_b", "node_c"])


graph = builder.compile()

result = graph.invoke({"x":12})
print(result)

png_byte = graph.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_byte)

print("graph.png saved!")


