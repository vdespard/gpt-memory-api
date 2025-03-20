from fastapi import FastAPI, HTTPException
from database import SessionLocal, Property
from vector_db import store_memory, retrieve_memory

app = FastAPI()

@app.get("/get_property/")
def get_property(name: str):
    """Retrieve structured data from SQL."""
    db = SessionLocal()
    property = db.query(Property).filter(Property.name == name).first()
    if property:
        return property
    raise HTTPException(status_code=404, detail="Property not found.")

@app.post("/add_property/")
def add_property(property: Property):
    """Add structured data to SQL."""
    db = SessionLocal()
    db.add(property)
    db.commit()
    return {"message": "Property added successfully!"}

@app.post("/add_memory/")
def add_memory(user_input: str, gpt_response: str):
    """Store conversation embeddings in Pinecone."""
    store_memory(user_input, gpt_response)
    return {"message": "Memory stored!"}

@app.get("/search_memory/")
def search_memory(query: str):
    """Retrieve past conversation memory from Pinecone."""
    results = retrieve_memory(query)
    return results
