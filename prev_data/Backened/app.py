from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import Ollama
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import torch

app = FastAPI()


def load_multiple_pdf(pdf_paths):
    all_doc = []
    for pdf_path in pdf_paths:
        loader = PyMuPDFLoader(pdf_path)
        doc = loader.load()
        all_doc.extend(doc) 
    return all_doc

def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(documents)
    return chunks

def load_embedding_model(model_path, normalize_embedding=True):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    return HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs={'device':'gpu'}, # here we will run the model with CPU only
        encode_kwargs = {
            'normalize_embeddings': normalize_embedding # keep True to compute cosine similarity
        }
    )
    

def create_embeddings(chunks, embedding_model, storing_path="vectorstore"):
    # Creating the embeddings using FAISS
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    
    # Saving the model in current directory
    vectorstore.save_local(storing_path)
    
    # returning the vectorstore
    return vectorstore

llm = Ollama(model = "llama3.1:8b", temperature=0)
embed = load_embedding_model(model_path="all-MiniLM-L6-v2")


pdf_files = ["TestData\career and course guidance.pdf","TestData\Carrier Guidance_converted.pdf"]
docs = load_multiple_pdf(pdf_files)
documents = split_docs(documents=docs)


vectorstore = create_embeddings(documents,embed)
retriever = split_docs(documents=docs)


# Define the contextualization system prompt
contextualize_q_system_prompt = """
Given a chat history and the latest user question which might reference context in the chat history,
formulate a standalone question which can be understood without the chat history.
Do NOT answer the question, just reformulate it if needed and otherwise return it as is.
"""
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

# Create history-aware retriever
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)


qa_system_prompt = """
### System:
You are WoxsenWay Chatbot, an AI voice Assistant for Woxsen University Career Guidance. Your goal is to provide clear and concise responses to students' career-related queries. \
Answer using only the information in the context, and keep your response within one or two sentences. If the answer is not available, simply say "I don't have that information."

### Context:
{context}

""" 

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

# Create question-answer chain
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

# Combine the retriever and QA chain
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# Statefully manage chat history
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

# Define a Pydantic model for the API request body
class QueryModel(BaseModel):
    query: str
    session_id: str

# Define an API endpoint for asking the LLM a question
@app.post("/ask")
async def ask_llm(query: QueryModel):
    # Retrieve session history and run the chain
    history = get_session_history(query.session_id)
    response = conversational_rag_chain.invoke(
        input={"input": query.query, "chat_history": history.messages}
    )
    
    print(response)  # Log the response for debugging
    return {"response": response["answer"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000, reload=True)