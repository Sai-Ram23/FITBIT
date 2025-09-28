# ui/login.py
import tkinter as tk
from tkinter import messagebox
import re
import sys
import os

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.auth.authentication import Authentication

class LoginWindow:
    def __init__(self, on_success_callback=None):
        self.window = tk.Tk()
        self.window.title("FITBIT - Login")
        self.window.configure(bg="white")
        self.auth = Authentication()
        self.on_success_callback = on_success_callback
        self.current_username = None  # Track logged-in user
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="FITBIT", font=("Arial", 40, "bold"), bg="black", fg="white").pack(pady=40)
        tk.Label(self.window, text="Username:", bg="white").pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()
        tk.Label(self.window, text="Password:", bg="white").pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()
        tk.Button(self.window, text="Login", command=self.validate_credentials, bg="orange", fg="white").pack(pady=10)
        tk.Button(self.window, text="Sign Up", command=self.signup_dialog, bg="green", fg="white").pack(pady=5)
        self.error_label = tk.Label(self.window, text="", fg="red", bg="white")
        self.error_label.pack(pady=5)

    def validate_credentials(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        if not username or not password:
            self.error_label.config(text="Username and password cannot be empty")
            return
        if not re.match(r'^[a-zA-Z0-9._-]+$', username):
            self.error_label.config(text="Invalid username format")
            return
        if self.auth.validate_credentials(username, password):
            self.current_username = username
            self.error_label.config(text="Login successful")
            if self.on_success_callback:
                self.on_success_callback(username)  # Pass username to callback
            self.window.withdraw()
        else:
            self.error_label.config(text="Invalid username or password")

    def signup_dialog(self):
        signup_window = tk.Toplevel(self.window)
        signup_window.title("Sign Up")
        signup_window.configure(bg="white")

        tk.Label(signup_window, text="Username:").pack()
        su_username = tk.Entry(signup_window)
        su_username.pack()
        tk.Label(signup_window, text="Password:").pack()
        su_password = tk.Entry(signup_window, show="*")
        su_password.pack()
        tk.Label(signup_window, text="Age:").pack()
        su_age = tk.Entry(signup_window)
        su_age.pack()
        tk.Label(signup_window, text="Weight (kg):").pack()
        su_weight = tk.Entry(signup_window)
        su_weight.pack()
        tk.Label(signup_window, text="Goals (e.g., weight loss):").pack()
        su_goals = tk.Entry(signup_window)
        su_goals.pack()
        tk.Button(signup_window, text="Register", command=lambda: self.register(su_username.get().strip(), su_password.get(), su_age.get(), su_weight.get(), su_goals.get(), signup_window)).pack(pady=10)

    def register(self, username, password, age_str, weight_str, goals, signup_window):
        try:
            age = int(age_str) if age_str else None
            weight = float(weight_str) if weight_str else None
            if self.auth.register_user(username, password, age, weight, goals):
                messagebox.showinfo("Success", "User registered successfully")
                signup_window.destroy()
            else:
                messagebox.showerror("Error", "Registration failed")
        except ValueError:
            messagebox.showerror("Error", "Invalid age or weight format")

    def run(self):
        self.window.mainloop()