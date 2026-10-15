import os
import psycopg2

conn = psycopg2.connect(
    host="postgres",
    user="postgres",
    password=os.environ.get("DB_PASS")
)

cur = conn.cursor()
cur.execute("SELECT version();")
print("Ответ базы:", cur.fetchone()[0])

conn.close()
