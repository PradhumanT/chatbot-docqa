from app.loader import load_documents
from app.splitter import split_documents
from app.embeddings import get_embedding_model
from app.vector_store import save_to_vectorstore, load_vectorstore
from app.chatbot import build_qa_chain

def main():
    # You can switch between loading and saving easily
    use_existing_index = True

    embedding_model = get_embedding_model()

    if use_existing_index:
        vectorstore = load_vectorstore(embedding_model)
    else:
        documents = load_documents("/Users/praddy/Documents/CODE/learning_langchain_folder/chatbot-docqa/data/attention.pdf")
        chunks = split_documents(documents)
        vectorstore = save_to_vectorstore(chunks, embedding_model)

    qa_chain = build_qa_chain(vectorstore)

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        result = qa_chain.invoke({"query": query})
        print("\nAnswer:\n", result["result"])

if __name__ == "__main__":
    main()
