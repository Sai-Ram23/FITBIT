# integrations/fitbit.py
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import sys

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

load_dotenv()

# Simple mapping for common activity IDs (expand as needed)
ACTIVITY_IDS = {
    "Running": 90013,
    "Walking": 90011,
    "Swimming": 90010,
    "Weight Lifting": 90008,
    "Cycling": 90009,
    "HIIT": 52000,  # Generic cardio
    "Yoga": 90007,
    # Add more from Fitbit docs
}

def log_workout_with_fitbit(workout_name, duration):
    fitbit_token = os.getenv("FITBIT_ACCESS_TOKEN")
    if not fitbit_token:
        print("Warning: Fitbit token not configured. Skipping API log.")
        return
    base_url = "https://api.fitbit.com/1/user/-/activities.json"
    headers = {"Authorization": f"Bearer {fitbit_token}"}
    
    # Use activityId if available, else fallback to name
    activity_id = ACTIVITY_IDS.get(workout_name, None)
    payload = {
        "activityId": activity_id,
        "startTime": "12:00:00",  # Placeholder; use dynamic in production
        "date": datetime.now().strftime("%Y-%m-%d"),
        "duration": duration * 60000  # Fixed: Milliseconds, not minutes
    }
    # Remove None keys for clean JSON
    payload = {k: v for k, v in payload.items() if v is not None}
    if not activity_id:
        payload["activityName"] = workout_name

    response = requests.post(base_url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Successfully logged '{workout_name}' to Fitbit")
    else:
        print(f"Fitbit API error: {response.status_code} - {response.text}")