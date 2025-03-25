import os
import pinecone
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="gcp-starter")

index = pinecone.Index(os.getenv("PINECONE_INDEX_NAME"))

def get_embedding(text: str):
    # Assuming you're using OpenAI to embed text
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    embedding = client.embeddings.create(input=[text], model="text-embedding-ada-002")
    return embedding.data[0].embedding

def search_property_embeddings(query: str):
    vector = get_embedding(query)
    result = index.query(vector=vector, top_k=5, include_metadata=True)
    return result.to_dict()
