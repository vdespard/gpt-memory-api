from pydantic import BaseModel

# ✅ Pydantic schema for API responses
class PropertySchema(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        orm_mode = True  # Allows conversion from SQLAlchemy model
