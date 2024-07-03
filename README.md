# Streamlit Chatbot with LangChain and OpenAI

This project demonstrates a simple chatbot application using Streamlit, LangChain, and OpenAI's GPT models. The chatbot responds to user queries by leveraging a language model and prompt template, providing helpful and accurate responses.

## Features

- *Streamlit Interface*: A user-friendly web interface for interacting with the chatbot.
- *LangChain Integration*: Utilizes LangChain for prompt management and model chaining.
- *OpenAI GPT Model*: Leverages OpenAI's GPT-3.5-turbo model for generating responses.

## Installation

1. *Clone the repository:*

   Clone this repository to your local machine.

2. *Set up a virtual environment:*

   Create and activate a virtual environment for dependency management.

3. *Install dependencies:*

   Install the required Python packages using pip.

4. *Environment Variables:*

   Create a .env file in the project directory and add your OpenAI and LangChain API keys. Ensure the following variables are set:
   - OPENAI_API_KEY
   - LANGCHAIN_API_KEY

## Usage

Run the Streamlit app using the Streamlit CLI. Open your web browser and navigate to the displayed local URL to interact with the chatbot.

## Error Handling

The application includes basic error handling for common issues such as rate limits and model access errors. Appropriate messages are displayed to inform the user about these issues.

## License

This project is licensed under the MIT License.
