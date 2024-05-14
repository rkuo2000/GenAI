#!/usr/bin/env python
# LlamaIndex-RAG Community Q&A system

# [Github](https://github.com/run-llama/llama_index)
# pip install llama_index transformers accelerate bitsandbytes -q
# pip install llama-index-llms-huggingface -q
# pip install llama-index-embeddings-langchain -q


## Setup LLM
import json
import torch
from transformers import BitsAndBytesConfig
from llama_index.core import PromptTemplate
from llama_index.llms.huggingface import HuggingFaceLLM

from langchain.embeddings import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.core import ServiceContext, Document
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.legacy.response.notebook_utils import display_response

from fastapi import FastAPI, Request
from fastapi.responses import Response
import uvicorn

from pydantic import BaseModel

# set quantization config
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

model_name = "taide/Llama3-TAIDE-LX-8B-Chat-Alpha1"

llm = HuggingFaceLLM(
    model_name=model_name,
    tokenizer_name=model_name,
    query_wrapper_prompt=PromptTemplate("<s>[INST] {query_str} [/INST] </s>\n"),   
    context_window=3900,
    max_new_tokens=256,
    model_kwargs={"quantization_config": quantization_config},    
    # tokenizer_kwargs={},
    generate_kwargs={"temperature": 0.2, "top_k": 5, "top_p": 0.95 , "do_sample": True},
    device_map="auto",
)

## Choosing the embedding model
# BAAI/bge-small-en-v1.5
# GanymedeNil/text2vec-large-chinese

#lc_embed_model = HuggingFaceEmbeddings(model_name=BAAI/bge-small-en-v1.5") # For English
lc_embed_model = HuggingFaceEmbeddings(model_name="GanymedeNil/text2vec-large-chinese") # For Chinese
embed_model = LangchainEmbedding(lc_embed_model)


service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

## Building a local VectorIndex

#from llama_index.readers import BeautifulSoupWebReader
#url = "https://www.theverge.com/2023/9/29/23895675/ai-bot-social-network-openai-meta-chatbots"
#documents = BeautifulSoupWebReader().load_data([url])

documents = SimpleDirectoryReader("./docs/community/").load_data()
vector_index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

query_engine = vector_index.as_query_engine()

## FastAPI for HTTP server

app = FastAPI()

class UserData(BaseModel):
    text: str

@app.get("/")
def root():
    return Response("Hello World!")

@app.get("/query/{query}")
def chat(query: str):
    prompt = query
    print(prompt)

    response = query_engine.query(prompt)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
