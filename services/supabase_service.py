from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_property_by_id(property_id: str):
    result = supabase.table("properties").select("*").eq("id", property_id).execute()
    return result.data[0] if result.data else None

def add_property(data: dict):
    return supabase.table("properties").upsert(data).execute()
