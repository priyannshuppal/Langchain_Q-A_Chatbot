#LANGCHAIN_API_KEY="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"
#OPEN_API_KEY=""
#LANGCHAIN_PROJECT="LANGCHAIN_Q&A_CHATBOT"
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
#env variables call
#langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
#craeting chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.Please provide response to the user queries"),
        ("user","Question:{question}")
    ]
)
# streamlit framework
st.title("Langchain Chatbot with Ollama Llama2")
input_text=st.text_input("Search the topic you want")

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
##chain
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text}))
