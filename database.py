from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Replace with your Supabase or PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:ARIs3TtZH12p4OZ9@db.tttvpvlcrutkajgtyybn.supabase.co:5432/postgres"

# ✅ Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# ✅ Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Scoped session (thread-safe)
db_session = scoped_session(SessionLocal)

# ✅ Base class for models
Base = declarative_base()

# ✅ Define the Property model
class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)

# ✅ Create database tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# ✅ Dependency to get a database session
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()