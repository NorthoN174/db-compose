import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres",
        database="postgres",
        user="postgres",
        password=os.environ.get("DB_PASS")
    )
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Создаем таблицу на всякий случай, если её нет
    cur.execute("CREATE TABLE IF NOT EXISTS history (id SERIAL PRIMARY KEY, run_time TIMESTAMP);")
    cur.execute("INSERT INTO history (run_time) VALUES (NOW());")
    conn.commit()
    
    # Забираем всю историю из базы
    cur.execute("SELECT id, run_time FROM history;")
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    
    # Красиво выводим на экран браузера
    html = "<h1>История запусков контейнера v2:</h1><ul>"
    for row in rows:
        html += f"<li>Запись №{row[0]} — время: {row[1]}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
