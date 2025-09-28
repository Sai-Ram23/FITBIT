# core/analytics.py
import sys
import os
from datetime import datetime

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.auth.authentication import Authentication
from integrations.gemini import analyze_trends

def log_and_analyze(username: str, workout_name: str, duration: int):
    auth = Authentication()
    date = datetime.now().strftime("%Y-%m-%d")
    auth.log_workout(username, workout_name, duration, date)
    return analyze_trends(username)

def get_personalized_recommendations(username: str, workout_name: str, duration: int):
    auth = Authentication()
    profile = auth.get_profile(username)
    logs = auth.get_user_logs(username)
    from integrations.gemini import generate_workout_recommendation
    return generate_workout_recommendation(workout_name, duration, profile, logs)