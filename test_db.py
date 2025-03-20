import psycopg2

DATABASE_URL = "postgresql://postgres:ARIs3TtZH12p4OZ9@db.tttvpvlcrutkajgtyybn.supabase.co:5432/postgres"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Database connection successful!")
    conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)
