# src/auth/authentication.py
import bcrypt
import sys
import os

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from .user_db import UserDB

class Authentication:
    def __init__(self):
        self.user_db = UserDB()

    def validate_credentials(self, username: str, password: str) -> bool:
        try:
            stored_hash = self.user_db.get_user_hash(username)
            if stored_hash and bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                return True
            return False
        except Exception:
            return False

    def register_user(self, username: str, password: str, age: int = None, weight: float = None, goals: str = None) -> bool:
        try:
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.user_db.add_user(username, password_hash)
            if age and weight and goals:
                self.user_db.add_or_update_profile(username, age, weight, goals)
            return True
        except Exception:
            return False

    def get_profile(self, username: str):
        return self.user_db.get_profile(username)

    def log_workout(self, username: str, workout_name: str, duration: int, date: str):
        self.user_db.log_workout(username, workout_name, duration, date)

    def get_user_logs(self, username: str, weeks_back: int = 1):
        return self.user_db.get_user_logs(username, weeks_back)