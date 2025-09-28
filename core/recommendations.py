# core/recommendations.py
import json
import os
import sys
from src.auth.authentication import Authentication

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def load_workout_config():
    config_path = os.path.join(os.path.dirname(__file__), "../config/workouts.json")
    with open(config_path, "r") as f:
        return json.load(f)

WORKOUT_CONFIG = load_workout_config()

def get_food_taken_for_workout(workout_name: str, duration: int, username: str = None) -> list[str]:
    # Base logic (as before, with parsing fix)
    config = WORKOUT_CONFIG.get(workout_name, {})
    food_taken = config.get("food_taken", {})
    for key, foods in food_taken.items():
        try:
            if '-' in key:
                parts = key.split('-')
                min_dur = float(parts[0]) if parts[0] != 'inf' else float('inf')
                max_dur = float('inf') if len(parts) > 1 and parts[1] == 'inf' else float(parts[1])
            if min_dur <= duration <= max_dur:
                # Personalize: Adjust for profile (e.g., low-cal for weight loss)
                if username:
                    auth = Authentication()
                    profile = auth.get_profile(username)
                    if profile and 'weight loss' in profile.get('goals', '').lower():
                        # Simple adjustment example
                        foods = [f.replace('smoothie', 'low-cal smoothie') for f in foods]
                return foods
        except (ValueError, IndexError):
            continue
    return []

def get_water_intake_for_workout(workout_name: str, username: str = None) -> int:
    config = WORKOUT_CONFIG.get(workout_name, {})
    intake = config.get("water_intake", 0)
    # Personalize: Scale by weight if profile available
    if username:
        auth = Authentication()
        profile = auth.get_profile(username)
        if profile and profile.get('weight'):
            intake = int(intake * (profile['weight'] / 70))  # Normalize to 70kg average
    return max(500, intake)  # Minimum 500ml