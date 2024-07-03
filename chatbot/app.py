from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

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
llm = ChatOpenAI(model="gpt-4o-turbo")
output_parser = StrOutputParser()

# Create chain
chain = prompt | llm | output_parser

# Invoke chain if input_text is provided
if input_text:
    try:
        result = chain.invoke({'question': input_text})
        st.write(result)
    except Exception as e:
        error_message = str(e)
        if '429' in error_message or 'RateLimitError' in error_message:
            st.error("Rate limit exceeded. Please check your API quota and try again later.")
        else:
            st.error(f"An error occurred: {error_message}")
