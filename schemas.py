from pydantic import BaseModel

# ✅ Pydantic schema for API responses
class PropertySchema(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        from_attributes = True  # ✅ Updated for Pydantic V2
