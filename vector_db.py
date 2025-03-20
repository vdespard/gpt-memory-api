import pinecone
import openai

# Pinecone API Key
PINECONE_API_KEY = "your_pinecone_api_key"
pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")

# Create or connect to an index
index_name = "gpt-memory"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536, metric="cosine")

index = pinecone.Index(index_name)

# OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key"

def store_memory(user_input, gpt_response):
    """Convert text to embeddings and store in Pinecone"""
    embedding = openai.Embedding.create(input=user_input, model="text-embedding-ada-002")["data"][0]["embedding"]
    index.upsert([(user_input, embedding)])

def retrieve_memory(query):
    """Retrieve similar past conversations"""
    embedding = openai.Embedding.create(input=query, model="text-embedding-ada-002")["data"][0]["embedding"]
    results = index.query([embedding], top_k=3, include_metadata=True)
    return results["matches"]
