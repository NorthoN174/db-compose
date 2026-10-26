import os
import psycopg2

conn = psycopg2.connect(
    host="postgres",
    user="postgres",
    password=os.environ.get("DB_PASS")
)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS runs (id SERIAL PRIMARY KEY, created_at TIMESTAMP DEFAULT NOW());")
cur.execute("INSERT INTO runs DEFAULT VALUES;")
conn.commit()

cur.execute("SELECT * FROM runs;")
print("История запусков:", cur.fetchall())

conn.close()
