# src/auth/user_db.py
import sqlite3
import os
import sys

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

class UserDB:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'users.db')
        self._initialize_db()

    def _initialize_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Users table (existing)
            cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (username TEXT PRIMARY KEY, password_hash TEXT)''')
            # Profiles table with migration (existing)
            cursor.execute('''CREATE TABLE IF NOT EXISTS profiles 
                            (username TEXT PRIMARY KEY, age INTEGER, weight REAL, goals TEXT,
                             FOREIGN KEY (username) REFERENCES users (username))''')
            cursor.execute("PRAGMA table_info(profiles)")
            columns = [col[1] for col in cursor.fetchall()]
            if 'age' not in columns:
                cursor.execute("ALTER TABLE profiles ADD COLUMN age INTEGER")
            if 'weight' not in columns:
                cursor.execute("ALTER TABLE profiles ADD COLUMN weight REAL")
            if 'goals' not in columns:
                cursor.execute("ALTER TABLE profiles ADD COLUMN goals TEXT")
            # Workout logs table with migration for 'date'
            cursor.execute('''CREATE TABLE IF NOT EXISTS workout_logs 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, workout_name TEXT,
                             duration INTEGER, date TEXT,
                             FOREIGN KEY (username) REFERENCES users (username))''')
            cursor.execute("PRAGMA table_info(workout_logs)")
            columns = [col[1] for col in cursor.fetchall()]
            if 'date' not in columns:
                cursor.execute("ALTER TABLE workout_logs ADD COLUMN date TEXT")
            conn.commit()

    def add_user(self, username: str, password_hash: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO users (username, password_hash) VALUES (?, ?)", 
                          (username, password_hash))
            conn.commit()

    def get_user_hash(self, username: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            return result[0] if result else None

    def add_or_update_profile(self, username: str, age: int, weight: float, goals: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO profiles (username, age, weight, goals) VALUES (?, ?, ?, ?)",
                          (username, age, weight, goals))
            conn.commit()

    def get_profile(self, username: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT age, weight, goals FROM profiles WHERE username = ?", (username,))
            result = cursor.fetchone()
            return {"age": result[0], "weight": result[1], "goals": result[2]} if result else None

    def log_workout(self, username: str, workout_name: str, duration: int, date: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO workout_logs (username, workout_name, duration, date) VALUES (?, ?, ?, ?)",
                          (username, workout_name, duration, date))
            conn.commit()

    def get_user_logs(self, username: str, weeks_back: int = 1):
        from datetime import datetime, timedelta
        end_date = datetime.now()
        start_date = end_date - timedelta(weeks=weeks_back)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT workout_name, duration, date FROM workout_logs 
                WHERE username = ? AND date >= ? ORDER BY date DESC
            """, (username, start_date.strftime("%Y-%m-%d")))
            return cursor.fetchall()