import os
from pinecone import Pinecone
import openai

# Load API keys from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Define the index name
index_name = "gpt-memory"

# Check if index exists, create if not
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,  # Adjust based on your embedding model
        metric="cosine",
        spec={"cloud": "aws", "region": "us-west-2"},
    )

# Connect to the index
index = pc.Index(index_name)

def store_memory(user_input, gpt_response):
    """Convert text to embeddings and store in Pinecone"""
    response = openai.Embedding.create(input=[user_input], model="text-embedding-ada-002")
    embedding = response["data"][0]["embedding"]
    
    index.upsert(vectors=[{"id": user_input, "values": embedding}])

def retrieve_memory(query):
    """Retrieve similar past conversations"""
    response = openai.Embedding.create(input=[query], model="text-embedding-ada-002")
    embedding = response["data"][0]["embedding"]
    
    results = index.query(vector=embedding, top_k=3, include_metadata=True)
    return results["matches"]
