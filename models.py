import sqlite3
from datetime import datetime

# 🔌 Connect to SQLite database
def get_connection():
    return sqlite3.connect('database.db')

# 🏗️ Create the database table
def init_db():
    print("[INFO] Initializing database...")
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                access_count INTEGER DEFAULT 0
            );
        ''')
    print("[INFO] Database initialized.")

# 🔗 Insert a new short URL
def create_url(url, short_code, now):
    with get_connection() as conn:
        conn.execute('''
            INSERT INTO urls (url, short_code, created_at, updated_at)
            VALUES (?, ?, ?, ?)
        ''', (url, short_code, now, now))
        conn.commit()
    return {
        "url": url,
        "shortCode": short_code,
        "createdAt": now,
        "UpdatedAt": now
    }

# 🔍 Retrieve original URL by shortcode
def get_url(short_code):
    with get_connection() as conn:
        cur = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,))
        row = cur.fetchone()
        if row:
            return {
                "id": row[0],
                "url": row[1],
                "shortCode": row[2],
                "createdAt": row[3],
                "updatedAt": row[4]
            }

# 🛠️ Update a URL by shortcode
def update_url(short_code, new_url):
    now = datetime.utcnow().isoformat()
    with get_connection() as conn:
        cur = conn.execute('UPDATE urls SET url = ?, updated_at = ? WHERE short_code = ?', (new_url, now, short_code))
        if cur.rowcount == 0:
            return None
        return get_url(short_code)

# 🗑️ Delete a short URL
def delete_url(short_code):
    with get_connection() as conn:
        cur = conn.execute('DELETE FROM urls WHERE short_code = ?', (short_code,))
        return cur.rowcount > 0

# ➕ Increment access counter
def increment_access(short_code):
    with get_connection() as conn:
        conn.execute('UPDATE urls SET access_count = access_count + 1 WHERE short_code = ?', (short_code,))
        conn.commit()

# 📊 Get access statistics
def get_stats(short_code):
    with get_connection() as conn:
        cur = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,))
        row = cur.fetchone()
        if row:
            return {
                "id": row[0],
                "url": row[1],
                "shortCode": row[2],
                "createdAt": row[3],
                "updatedAt": row[4],
                "accessCount": row[5]
            }
