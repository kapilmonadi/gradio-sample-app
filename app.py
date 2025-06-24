import gradio as gd

def sayHello(name: str):
    return f"Hello {name}"

ui=gd.Interface(fn=sayHello, inputs="textbox", outputs="textbox")
ui.launch()