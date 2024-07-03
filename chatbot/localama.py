from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os
from dotenv import load_dotenv 

# Load environment variables from the .env file
load_dotenv()

# Set environment variables for API keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")  # Fixed typo

# Create prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit app setup
st.title("Demo")
input_text = st.text_input("Search topic")

# Initialize LLM and output parser
llm = ChatOpenAI(model="llama-2")
output_parser = StrOutputParser()

# Create chain
chain = prompt | llm | output_parser
