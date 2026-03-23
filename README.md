## ChatGPT Clone (Streamlit + OpenAI)
A simple ChatGPT-like web app built using Streamlit and the OpenAI API.
This app allows users to have real-time conversations with an AI assistant in a clean chat interface.
## Project Features
1. Chat-based UI (like ChatGPT) 
2. Context-aware conversations (chat history maintained) 
3. Fast responses using gpt-4.1-mini 
4. Persistent session using Streamlit session state 
5. Clean and minimal interface 
## Tech Stack
	Frontend/UI: Streamlit 
	Backend: Python 
	LLM API: OpenAI 
	Environment Management: python-dotenv 
## Project Structure
	.
	├── app.py          # Main Streamlit app
	├── .env            # API keys (not pushed to GitHub)
	├── requirements.txt
	└── README.md
## Installation
	1. Clone the repository
		git clone https://github.com/your-username/chatgpt-clone.git
		cd chatgpt-clone
## Create virtual environment (recommended)
	If using uv:
	
	uv venv
	uv pip install -r requirements.txt
	
	Or using pip:
	
	python -m venv .venv
	.venv\Scripts\activate   # Windows
	pip install -r requirements.txt
## Add your API key
	Create a .env file:
	OPENAI_API_KEY=your_api_key_here
## Run the App
	streamlit run app.py
	Then open your browser at:
	http://localhost:8501
## How It Works
1.	User enters a message in the chat input
2.	Message is stored in st.session_state
3.	Full conversation history is sent to OpenAI API
4.	AI generates a response
5.	Response is displayed and stored 
## Code Highlights
	Session State (Memory)
	if "messages" not in st.session_state:
		st.session_state.messages = []
## OpenAI API Call
	response = client.chat.completions.create(
		model="gpt-4.1-mini",
		messages=st.session_state.messages,
		temperature=0.7
	)
## Chat UI
	with st.chat_message("assistant"):
		st.markdown(reply)

