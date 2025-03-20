from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your Supabase or PostgreSQL connection string
DATABASE_URL = "postgresql://your_user:your_password@your_db_host:5432/your_db_name"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    num_units = Column(Integer)
    unit_type = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    square_footage = Column(Integer)
    rent_per_month = Column(DECIMAL)

Base.metadata.create_all(bind=engine)
