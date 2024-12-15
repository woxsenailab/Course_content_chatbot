from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
#from langchain_community.chains import RetrievalQA
import textwrap
#import chain


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
    return HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs={'device':'cpu'}, # here we will run the model with CPU only
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



# prompt_template = """
# ### System:
# You are WoxsenWay Chatbot, an AI voice Assistant for Woxsen University Career Guidance. Your goal is to provide clear and concise responses to students' career-related queries. \
# Answer using only the information in the context, and keep your response within one or two sentences. If the answer is not available, simply say "I don't have that information."

# ### Context:
# {context}

# ### User:
# {question}

# ### Response:
# """





