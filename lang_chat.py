from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from typing import Optional

app = FastAPI(
    title="LangChain ChatBot API",
    description="A conversational AI chatbot using LangChain and OpenAI",
    version="1.0.0"
)

# Single conversation instance for one user
conversation_chain: Optional[ConversationChain] = None

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class OpenAIChatbot:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=""
        )
    
    def create_conversation(self) -> ConversationChain:
        """Create a new conversation chain with memory"""
        memory = ConversationBufferMemory()
        return ConversationChain(
            llm=self.llm,
            memory=memory,
            verbose=False
        )

# Initialize chatbot
chatbot = OpenAIChatbot()

@app.post("/api/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(chat_request: ChatRequest):
    """
    Send a message to the AI chatbot
    
    - **message**: Your message to the AI
    """
    global conversation_chain
    
    try:
        # Create conversation if it doesn't exist
        if conversation_chain is None:
            conversation_chain = chatbot.create_conversation()
        
        # Get AI response
        response = conversation_chain.predict(input=chat_request.message)
        
        return ChatResponse(response=response)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)