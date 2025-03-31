from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from app.config import PINECONE_API_KEY, INDEX_NAME, NAMESPACE

def init_pinecone():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

def save_to_vectorstore(docs, embedding):
    init_pinecone()
    return PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embedding,
        index_name=INDEX_NAME,
        namespace=NAMESPACE
    )

def load_vectorstore(embedding):
    return PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embedding,
        namespace=NAMESPACE
    )
