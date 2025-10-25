LangChain Chatbot with Ollama LLaMA 2

A simple Q&A chatbot built using LangChain, Ollama LLaMA 2, and Streamlit. The chatbot answers user queries based on a conversational AI model running locally.

🚀 Features

-->Uses LLaMA 2 model via Ollama for offline, local inference.

-->Built with LangChain prompt templates for structured conversations.

-->Streamlit-based web interface for easy interaction.

-->Lightweight, runs entirely locally on macOS.

🛠️ Requirements

Python 3.10+

-->Ollama installed on your system (https://ollama.com/
)

-->Virtual environment (recommended)

Python packages (from requirements.txt):

-->langchain_openai
-->langchain_core
-->python-dotenv
-->streamlit
-->langchain_community
-->langserve

⚡ Installation




Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


Set environment variables
Create a .env file in the project root:

LANGCHAIN_API_KEY=<your_langchain_api_key>




🖥️ Running the Chatbot
==streamlit run app.py


Enter your query in the input box and see the chatbot response.



💡 Usage Example


User: What is LangChain?'

Bot: LangChain is a framework for building applications with LLMs...

⚙️ Notes

Make sure Ollama is installed and added to PATH so that ollama works in the terminal.

LLaMA 2 model runs locally, so responses are faster and do not require API calls.

This setup works on macOS; Windows/Linux may require minor adjustments.
