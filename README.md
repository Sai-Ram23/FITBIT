# Fitbit AI Workout Logger

## Overview
The Fitbit AI Workout Logger is a modular, AI-enhanced desktop application built with Python and Tkinter for tracking workouts, generating personalized recommendations, and integrating with Fitbit and Google's Gemini API. It supports multi-user profiles, secure authentication, data analytics, and visualizations, making it a comprehensive fitness companion.

## Key Features
- > Secure Authentication: User login/signup with bcrypt-hashed passwords and SQLite storage. Multi-user support with profile data (age, weight, goals) for personalization.
- > Workout Logging: Log workouts with name and duration; auto-generates food/water intake recommendations from a JSON config.
- > AI Personalization (Gemini Integration): Tailored tips and plans based on profile/history using Google's Gemini API (e.g., "recovery advice for weight loss goals").
- > Chat Interface: Real-time "Ask AI" chat for workout queries, leveraging user profile for context-aware responses.
- > Fitbit API Sync: Logs workouts to Fitbit (dual-mode: real/simulated based on token).
- > Data Analytics: Stores logs in SQLite; Gemini analyzes trends (e.g., weekly summaries and improvements).
- > Visualizations: Matplotlib-embedded charts for workout trends (e.g., bar graphs of duration over time) with AI insights.
- > Modular Architecture: Separation of concerns (UI, core logic, integrations, auth) for maintainability and testing.
- > The app operates in dual mode: Core features work offline (JSON/DB), while APIs enhance with real-time data.

## Prerequisites
Python 3.8+ (tested on 3.13).
Git for version control.
A Fitbit account for API access (optional for simulation mode).
Google AI Studio API key for Gemini (free tier sufficient).

## Installation
Clone the Repository:
```bash
git clone https://github.com/Sai-Ram23/FITBIT.git
cd FITBIT
```

# Create a Virtual Environment (Recommended):
```bash
python -m venv venv
```
# On Windows:
```bash
venv\Scripts\activate
```
# On macOS/Linux:
```bash
source venv/bin/activate
```

# Install Dependencies:
```bash
pip install -r requirements.txt
```

Configure Environment Variables:
```bash
new-item .env
```

Edit .env:
```bash
FITBIT_ACCESS_TOKEN=your_fitbit_access_token_here  # From Fitbit OAuth (optional)
GOOGLE_AI_API_KEY=your_gemini_api_key_here  # From https://aistudio.google.com/app/apikey
```

Note: Never commit .env (ignored in .gitignore).

Database Setup: The app auto-initializes users.db on first run (SQLite—no separate setup).
Run the Application:
```bash
python main.py
```

Signup with profile details → Login → Log workouts → Use chat/analytics.

# Usage
## Signup/Login:
Enter username/password.
On signup, provide age, weight (kg), goals (e.g., "weight loss").
Profiles personalize AI recommendations.

## Log a Workout:

Enter workout name (e.g., "Walking") and duration (minutes).
Click "Log Workout": Views static recs (food/water), Fitbit sync, personalized AI tip, and trend analysis.

## AI Chat:

Click "Ask AI Chat".
Type queries (e.g., "Tip for running?")—responses use your profile/history.

## Analytics & Visualizations:

Click "View Analytics & Chart": Displays Matplotlib bar chart of recent workouts + Gemini summary (e.g., "Increase cardio for goals").

AI Personalized Rec: [Gemini tip based on your age/weight/goals]
Trend Analysis: [Gemini summary of trends]
## Project Structure
```structure
FITBIT/
├── .env.example          # Secrets template
├── .gitignore            # Ignores .env, .db, etc.
├── main.py               # Entry point
├── requirements.txt      # Dependencies
├── config/
│   └── workouts.json     # Static food/water recs
├── ui/                   # Tkinter UIs
│   ├── login.py          # Auth UI with profile signup
│   ├── main.py           # Workout/chat/analytics UI
│   └── chat.py           # AI chat window
├── core/                 # Business logic
│   ├── recommendations.py # JSON-based recs (personalized)
│   └── analytics.py      # DB logging + Gemini analysis
├── integrations/         # APIs
│   ├── fitbit.py         # Fitbit logging
│   └── gemini.py         # Gemini prompts/chat
└── src/
    └── auth/             # Secure auth/DB
        ├── authentication.py
        └── user_db.py    # SQLite with migrations
    └── utils/
        ├──__init__.py
        └──logger.py
```

# Development Workflow
As a Git expert, follow this for contributions:
Branching: git checkout -b feature/[name] (e.g., feature/enhance-chat).
Commits: Semantic (e.g., git commit -m "feat: added profile validation").
PRs: Create GitHub PRs with descriptions; self-review for code quality.
Testing: Run python main.py; verify DB (sqlite3 users.db "SELECT * FROM workout_logs;").
Linting: Optional: 
```bash 
pip install pylint; pylint src/.
```

Known Limitations & Roadmap

Offline Mode: Full (JSON/DB); APIs optional.
Quotas: Monitor Gemini (15 RPM free) and Fitbit rates.
Roadmap:
- > Mobile export (CSV/PDF).
- > Advanced AI (e.g., full plans via Gemini).
- > Deployment: PyInstaller for .exe or Streamlit for web.

## Troubleshooting

API Errors: Check .env keys; regenerate if invalid.
DB Issues: Delete users.db and rerun (auto-migrates).
Matplotlib Backend: If charts fail, add matplotlib.use('TkAgg') to main.py imports.
Dependencies: Ensure Tkinter (built-in; on Linux: sudo apt install python3-tk).

## Contributing
Fork the repo, create a feature branch, and submit a PR. Follow PEP 8 for style.
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.