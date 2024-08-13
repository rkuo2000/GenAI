#!/usr/bin/env python

## [How to use CSV files in vector stores with Langchain](https://how.wtf/how-to-use-csv-files-in-vector-stores-with-langchain.html)
#pip install langchain
#pip install langchain-ollama
#sudo apt install libsqlite3-dev
#pip install pysqlite3

##　Langchain Expression with Chroma DB CSV (RAG)
## Setup LLM
import json
import torch
import sqlite3
import pandas as pd

from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from sqlalchemy.exc import OperationalError

from fastapi import FastAPI, Request
from fastapi.responses import Response
import uvicorn

from pydantic import BaseModel

csvfile = "docs/113-Q2.csv"

model_name = "snickers8523/llama3-taide-lx-8b-chat-alpha1-q4-0:latest"

model = OllamaLLM(model=model_name)


db = SQLDatabase.from_uri("sqlite:///./northwind.db")

## FastAPI for HTTP server

app = FastAPI()

class UserData(BaseModel):
    text: str

@app.get("/")
def root():
    return Response("Hello World!")

@app.get("/query/{query}")
def chat(query: str):
    question = query
    print(question)

    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain = (
    {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    result = chain.invoke(query)
    print(result)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
