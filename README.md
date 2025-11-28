# 🤖 Multi-Model AI Chatbot (LangChain + LlamaIndex)

This project is a Streamlit-based conversational AI chatbot that offers the unique ability to dynamically switch between two powerful Large Language Model (LLM) frameworks: LangChain and LlamaIndex. Designed for flexibility and a seamless user experience, it provides conversation memory, real-time model switching, and a clean, intuitive chat UI, all orchestrated from a single `app.py` file.

## 🚀 Features

### 🔄 Model Switching (Unique Feature)

The core innovation of this chatbot is its dynamic model switching capability. Users can easily toggle between:
* **LangChain** (leveraging OpenAI Chat Models)
* **LlamaIndex** (using its `SimpleChatEngine` with memory)

Each framework maintains its own isolated conversation memory buffer, and switching between them automatically resets the conversation state for the newly selected model, ensuring a clean slate or the ability to return to a previous context if implemented (currently resets).

### 💬 Full Chat Interface

Experience a complete and user-friendly chat environment built with Streamlit:
* **Interactive Chat UI**: A responsive and modern interface for natural conversations.
* **Conversation History**: Keeps track of previous messages within the active model's session.
* **Dynamic Responses**: AI responses are displayed in real-time.
* **Clean UI**: An aesthetically pleasing and easy-to-navigate design.

### 🧠 Memory Support

To ensure coherent and context-aware conversations, both integrated frameworks utilize robust memory mechanisms:
* **LangChain**: Employs `ConversationBufferMemory` to store and recall past conversational turns.
* **LlamaIndex**: Uses `ChatMemoryBuffer` for efficient memory management within its chat engine.

### 🔐 Secure API Key Handling

The application prioritizes secure handling of your OpenAI API keys, supporting:
* `st.secrets` for secure deployment on Streamlit Cloud.
* `.env` files for local development, preventing API keys from being hardcoded or committed to version control.

---

## 🏗️ Project Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/anuradha2504/IC-Conversational-Chatbot-Lanchain-llamaIndex/blob/main/System-architecture-flow-Chatbot-Langchain-LlamaIndex.png" />

🏁 Live Demo
🌍 Deployed Endpoint:
https://conversational-chatbot-langchain-llamaindix.streamlit.app/

🧠 Try both LangChain and LlamaIndex models from the dropdown in the UI.

📚 Example Output
🔹 LangChain Chat
<img width="1231" height="569" alt="image" src="https://github.com/user-attachments/assets/76663c08-e5d9-449b-9ddb-cc15a170f767" />

🔹 LlamaIndex Chat
<img width="1110" height="635" alt="image" src="https://github.com/user-attachments/assets/d4b270fc-12b4-4905-94a0-a5dee5f48cf3" />




### Key Components:

* **User (🧑)**: Interacts with the chatbot via the Streamlit UI.
* **Streamlit UI (App Port 8000)**: The front-end application built with Streamlit, providing the chat interface, model switcher, and displaying responses. It serves as the primary interaction point.
* **LangChain Framework**:
    * **ConversationChain**: Manages the flow of conversation and integrates the LLM with memory.
    * **ConversationBufferMemory**: Stores the chat history for context within the LangChain session.
    * **OpenAI Chat Model (gpt-3.5-turbo)**: The underlying language model used by LangChain to generate responses.
* **LlamaIndex Framework**:
    * **SimpleChatEngine**: LlamaIndex's component for handling conversational interactions.
    * **ChatMemoryBuffer**: Manages chat history and context for LlamaIndex sessions.
    * **OpenAI Chat Model (gpt-3.5-turbo)**: The underlying language model used by LlamaIndex to generate responses.
* **OpenAI API (☁️)**: The external service that both LangChain and LlamaIndex frameworks use to communicate with the `gpt-3.5-turbo` model.
* **Secure API Key Handling (`st.secrets` / `.env`)**: Mechanism to securely access and use the OpenAI API key for authentication.

### Interaction Flow:

1.  **User Input**: The user types a message into the Streamlit UI.
2.  **Model Selection**: The user selects either "LangChain" or "LlamaIndex" from the model switcher.
3.  **Framework Interaction**: Based on the selection, the Streamlit UI directs the user's message to the appropriate framework (LangChain or LlamaIndex).
4.  **Memory Management**: Each framework retrieves its respective conversation history from its dedicated memory buffer.
5.  **LLM Interaction**: The selected framework sends the user's prompt (along with conversation history) to the OpenAI API.
6.  **Response Generation**: The OpenAI `gpt-3.5-turbo` model processes the prompt and generates a response.
7.  **Response Display**: The response is sent back to the Streamlit UI and displayed to the user.
8.  **Model Switching Logic**: If the user switches models, the current conversation state for the *previous* model is preserved (or effectively discarded if starting fresh for the new model), and the *new* model starts with its own, potentially empty, memory buffer.

## 🛠️ Technologies Used

* **Python**: The primary programming language.
* **Streamlit**: For creating the interactive web application and UI.
* **LangChain**: A framework for developing applications powered by language models.
* **LlamaIndex**: A data framework for LLM applications.
* **FastAPI**: (Used for the underlying API services, though integrated directly in `app.py` for simplicity in this Streamlit app context for the example code provided).
* **Pydantic**: For data validation with FastAPI.
* **OpenAI API**: For accessing GPT-3.5-turbo.
* **`python-dotenv`**: For managing environment variables in local development.
* **Uvicorn**: An ASGI web server (for local API testing if running the FastAPI components separately).

## 🚀 Getting Started

Follow these instructions to set up and run the chatbot locally.

### Prerequisites

* Python 3.8+
* An OpenAI API Key

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/multi-model-ai-chatbot.git](https://github.com/your-username/multi-model-ai-chatbot.git)
cd multi-model-ai-chatbot

** 2. Set Up a Virtual Environment (Recommended)**
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

**3. Install Dependencies**
pip install -r requirements.txt

**4. Configure Your OpenAI API Key**
Create a .env file in the root directory of your project and add your OpenAI API key:

OPENAI_API_KEY="your_openai_api_key_here"
For Streamlit Cloud Deployment: If deploying to Streamlit Cloud, you should use st.secrets. Add your API key in the app's secret management. Refer to the Streamlit documentation for st.secrets.

**5. Run the Streamlit Application**

streamlit run app.py
This will open the chatbot in your web browser (usually at http://localhost:8000).

**Project Structure**
.
├── app.py                  # Main Streamlit application with chatbot logic
├── .env                    # Environment variables (for local API key)
├── requirements.txt        # Python dependencies
└── README.md               # This README file
**💡 How to Use**
Open the Streamlit application in your browser.

You'll see a chat interface and a "Model Switcher" dropdown.

Select either "LangChain" or "LlamaIndex" from the dropdown.

Type your message in the input box and press Enter.

The chatbot will respond using the selected framework.

You can switch models at any time, and the conversation for the previously active model will be reset (or maintained if you implement more advanced memory switching logic).

**🤝 Contributing**
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

