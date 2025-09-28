# ui/main.py
import tkinter as tk
from tkinter import messagebox
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from core.recommendations import get_food_taken_for_workout, get_water_intake_for_workout
from integrations.fitbit import log_workout_with_fitbit
from integrations.gemini import generate_workout_recommendation
from core.analytics import log_and_analyze, get_personalized_recommendations
from ui.chat import ChatWindow
from src.auth.authentication import Authentication  # Fixed: Added missing import

class MainWindow:
    def __init__(self, username):
        self.window = tk.Tk()
        self.window.title("FITBIT")
        self.window.configure(bg="grey")
        self.username = username
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Workout Name:", bg="white", fg="black").grid(row=0, column=0, pady=20, padx=10, sticky="e")
        self.name_entry = tk.Entry(self.window, bg="white", fg="black")
        self.name_entry.grid(row=0, column=1, pady=20, padx=10, sticky="w")

        tk.Label(self.window, text="Duration (minutes):", bg="white", fg="black").grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.duration_entry = tk.Entry(self.window, bg="white", fg="black")
        self.duration_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        tk.Button(self.window, text="Log Workout", command=self.log_workout, bg="white", fg="black").grid(row=2, column=0, columnspan=2, pady=20)
        tk.Button(self.window, text="Ask AI Chat", command=self.open_chat, bg="blue", fg="white").grid(row=2, column=2, pady=20)
        tk.Button(self.window, text="View Analytics & Chart", command=self.show_analytics, bg="green", fg="white").grid(row=2, column=3, pady=20)

        self.workout_text = tk.Text(self.window, height=15, width=60, bg="white", fg="black", font="Arial")
        self.workout_text.grid(row=3, column=0, columnspan=4, padx=20)

        self.chart_frame = tk.Frame(self.window, height=300, width=600)
        self.chart_frame.grid(row=4, column=0, columnspan=4, pady=10)
        self.chart_frame.pack_propagate(False)  # Fixed: Use propagate to control sizing

    def log_workout(self):
        workout_name = self.name_entry.get().strip()
        duration_str = self.duration_entry.get().strip()
        if not duration_str.isdigit() or int(duration_str) <= 0:
            self.workout_text.insert(tk.END, "Error: Invalid duration\n")
            return
        duration = int(duration_str)

        self.workout_text.insert(tk.END, f"Workout Name: {workout_name}\n")
        self.workout_text.insert(tk.END, f"Duration: {duration} minutes\n")
        self.workout_text.insert(tk.END, "------------------------\n")

        # Personalized recommendations
        food_taken = get_food_taken_for_workout(workout_name, duration, self.username)
        water_intake = get_water_intake_for_workout(workout_name, self.username)

        self.workout_text.insert(tk.END, "Food_taken:\n")
        for meal in food_taken:
            self.workout_text.insert(tk.END, f"- {meal}\n")

        self.workout_text.insert(tk.END, f"Water Intake: {water_intake} ml\n")
        self.workout_text.insert(tk.END, "------------------------\n")

        log_workout_with_fitbit(workout_name, duration)
        self.workout_text.insert(tk.END, "Workout logged to Fitbit\n")

        # Log to DB and get AI rec
        trend_analysis = log_and_analyze(self.username, workout_name, duration)
        personalized_rec = get_personalized_recommendations(self.username, workout_name, duration)
        self.workout_text.insert(tk.END, f"AI Personalized Rec: {personalized_rec}\n")
        self.workout_text.insert(tk.END, f"Trend Analysis: {trend_analysis}\n")
        self.workout_text.insert(tk.END, "------------------------\n")

    def open_chat(self):
        ChatWindow(self.username).show()

    def show_analytics(self):
        auth = Authentication()  # Fixed: Now imported
        logs = auth.get_user_logs(self.username)
        if not logs:
            messagebox.showinfo("Info", "No workout data yet.")
            return

        # Matplotlib chart: Duration over time
        dates = [log[2] for log in logs]
        durations = [log[1] for log in logs]
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(dates, durations)
        ax.set_xlabel('Date')
        ax.set_ylabel('Duration (min)')
        ax.set_title('Weekly Workout Trends')

        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # AI insights
        from integrations.gemini import analyze_trends  # Ensure import for insights
        insights = analyze_trends(self.username)
        self.workout_text.insert(tk.END, f"Chart Insights (AI): {insights}\n")

    def show(self):
        self.window.deiconify()

    def withdraw(self):
        self.window.withdraw()

if __name__ == "__main__":
    MainWindow("testuser").show()
    tk.mainloop()