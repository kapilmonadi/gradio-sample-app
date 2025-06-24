import gradio as gd

def sayHello(name: str):
    return f"Hello {name}"

ui=gd.Interface(fn=sayHello, inputs="textbox", outputs="textbox", allow_flagging="never")
ui.launch(share=True)