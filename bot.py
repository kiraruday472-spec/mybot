import sqlite3

conn = sqlite3.connect("neobox.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    username TEXT,
    registered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    wallet REAL DEFAULT 0
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_key TEXT UNIQUE,
    title TEXT,
    upload_by INTEGER,
    upload_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    url TEXT,
    total_plays INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()
print("✅ Database ban gaya: neobox.db")
