from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from app.config import GOOGLE_API_KEY

def get_prompt_template():
    return PromptTemplate.from_template(
        """You are a helpful assistant. Use only the information from the context below to answer the question.
If the question cannot be answered using the context, say:
"I’m sorry, I cannot answer that based on the provided document."

<context>
{context}
</context>

Question: {question}
Answer:"""
    )

def build_qa_chain(vectorstore):
    # Gemini model
    llm = GoogleGenerativeAI(model="gemini-2.0-flash")
    prompt = get_prompt_template()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
