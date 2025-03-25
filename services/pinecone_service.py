import openai
import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pinecone.Index(os.getenv("PINECONE_INDEX_NAME"))

def embed_and_store(text: str, metadata: dict):
    try:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        embedding = response["data"][0]["embedding"]

        index.upsert([{
            "id": metadata.get("id", "unknown"),
            "values": embedding,
            "metadata": metadata
        }])

        return {"message": "Embedding stored"}
    except Exception as e:
        return {"error": str(e)}
