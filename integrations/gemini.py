# integrations/gemini.py
import google.generativeai as genai
import os
from dotenv import load_dotenv
from src.auth.authentication import Authentication
import sys

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

load_dotenv()

def configure_gemini():
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_AI_API_KEY not configured in .env")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

def generate_workout_recommendation(workout_name: str, duration: int, profile=None, logs=None) -> str:
    try:
        model = configure_gemini()
        profile_info = f"User profile: Age {profile.get('age', 'unknown')}, Weight {profile.get('weight', 'unknown')}kg, Goals: {profile.get('goals', 'general fitness')}" if profile else ""
        logs_info = f"Recent logs: {len(logs or [])} workouts" if logs else ""
        prompt = f"{profile_info}. {logs_info}. Generate a short tip for a {duration}-minute {workout_name} workout. Under 100 words."
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No recommendation generated."
    except Exception as e:
        return f"AI recommendation error: {str(e)}"

def generate_ai_response(username: str, query: str) -> str:
    try:
        model = configure_gemini()
        auth = Authentication()
        profile = auth.get_profile(username)
        logs = auth.get_user_logs(username)
        profile_info = f"Profile: Age {profile.get('age', 'unknown')}, Weight {profile.get('weight', 'unknown')}kg, Goals: {profile.get('goals', 'general')}" if profile else ""
        logs_summary = f"Recent workouts: {len(logs)} entries" if logs else ""
        prompt = f"{profile_info}. {logs_summary}. User query: {query}. Provide a helpful workout tip."
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No response generated."
    except Exception as e:
        return f"AI error: {str(e)}"

def analyze_trends(username: str, weeks_back: int = 1) -> str:
    try:
        model = configure_gemini()
        auth = Authentication()
        logs = auth.get_user_logs(username, weeks_back)
        if not logs:
            return "No workout data available."
        log_summary = "; ".join([f"{name} {dur}min on {date}" for name, dur, date in logs])
        prompt = f"Analyze these workouts: {log_summary}. Summarize trends and suggest 2-3 improvements. Keep concise."
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "Analysis unavailable."
    except Exception as e:
        return f"Analysis error: {str(e)}"