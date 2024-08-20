from typing import Any, Dict
from graph.state import GraphState
from ingestion_pinecone import retriever
from dotenv import load_dotenv

load_dotenv()


def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}
