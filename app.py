import os
import gradio as gr
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.globals import set_debug, set_verbose


set_debug(True) # enable debugging in Langchain
set_verbose(True)

def getLlamaModel():
    return ChatOllama(model="llama3.2")

def getGroqModel():
    return ChatGroq(model="mixtral-8x7b-32768")

def sayHello(name: str):
    return f"Hello {name}"

def get_response(query: str) -> str:
    response = llm.invoke(query)
    return response.content

# ui=gr.Interface(fn=sayHello, inputs="textbox", outputs="textbox", allow_flagging="never")
ui=gr.Interface(fn=get_response, inputs=[gr.Textbox(label="Input query", lines=5)],
                outputs=[gr.Textbox(label="Response", lines=10)], flagging_mode="never")
ui.launch(share=True)