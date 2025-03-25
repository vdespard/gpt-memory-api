from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.supabase_service import add_property, get_property_by_id
from services.pinecone_service import embed_and_store
from github import get_repo_info  # Optional GitHub route
from fastapi.responses import FileResponse

app = FastAPI()

# ✅ Models
class PropertyInput(BaseModel):
    id: str
    name: str
    units: int
    occupancy: float

class EmbedInput(BaseModel):
    text: str
    metadata: dict

# ✅ Supabase Endpoints
@app.post("/supabase/property")
async def add_property_supabase(prop: PropertyInput):
    result = add_property(prop.dict())
    return result

@app.get("/supabase/property/{property_id}")
async def get_property_supabase(property_id: str):
    result = get_property_by_id(property_id)
    if not result:
        raise HTTPException(status_code=404, detail="Property not found")
    return result

# ✅ Pinecone Embedding Endpoint
@app.post("/pinecone/embedding")
async def embed_text(req: EmbedInput):
    return embed_and_store(req.text, req.metadata)

# ✅ GitHub Info Route (optional)
@app.get("/github/{owner}/{repo}")
async def github_repo_info(owner: str, repo: str):
    return get_repo_info(owner, repo)

# ✅ Serve OpenAPI YAML for Custom GPT
@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    return FileResponse("openapi.yaml")

# ✅ Root Health Check
@app.get("/")
async def root():
    return {"message": "API is working!"}