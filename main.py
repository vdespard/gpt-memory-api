from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db, Property  # Import SQLAlchemy model and DB session
from schemas import PropertySchema  # Import Pydantic schema

app = FastAPI()

# ✅ GET all properties
@app.get("/properties", response_model=List[PropertySchema])
async def get_properties(db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    return properties

# ✅ GET a property by ID
@app.get("/properties/{property_id}", response_model=PropertySchema)
async def get_property(property_id: int, db: Session = Depends(get_db)):
    property_item = db.query(Property).filter(Property.id == property_id).first()
    if property_item is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_item

# ✅ CREATE a new property
@app.post("/properties", response_model=PropertySchema)
async def create_property(property_data: PropertySchema, db: Session = Depends(get_db)):
    new_property = Property(**property_data.dict())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property

# ✅ UPDATE an existing property
@app.put("/properties/{property_id}", response_model=PropertySchema)
async def update_property(property_id: int, updated_data: PropertySchema, db: Session = Depends(get_db)):
    property_item = db.query(Property).filter(Property.id == property_id).first()
    if property_item is None:
        raise HTTPException(status_code=404, detail="Property not found")

    for key, value in updated_data.dict().items():
        setattr(property_item, key, value)

    db.commit()
    db.refresh(property_item)
    return property_item

# ✅ DELETE a property
@app.delete("/properties/{property_id}")
async def delete_property(property_id: int, db: Session = Depends(get_db)):
    property_item = db.query(Property).filter(Property.id == property_id).first()
    if property_item is None:
        raise HTTPException(status_code=404, detail="Property not found")

    db.delete(property_item)
    db.commit()
    return {"message": "Property deleted successfully"}

# ✅ Root route
@app.get("/")
async def root():
    return {"message": "API is working!"}

