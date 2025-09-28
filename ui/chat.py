# ui/chat.py
import tkinter as tk
from tkinter import scrolledtext
import sys
import os

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from integrations.gemini import generate_ai_response  # Updated function for chat

class ChatWindow:
    def __init__(self, username):
        self.window = tk.Toplevel()
        self.window.title("Ask AI for Workout Tips")
        self.window.configure(bg="white")
        self.username = username
        self.setup_ui()

    def setup_ui(self):
        self.chat_display = scrolledtext.ScrolledText(self.window, height=15, width=50, bg="white", fg="black")
        self.chat_display.pack(pady=10, padx=10)
        self.input_entry = tk.Entry(self.window, width=50)
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<Return>", self.send_message)
        tk.Button(self.window, text="Send", command=self.send_message, bg="blue", fg="white").pack(pady=5)

    def send_message(self, event=None):
        query = self.input_entry.get().strip()
        if not query:
            return
        self.chat_display.insert(tk.END, f"You: {query}\n")
        response = generate_ai_response(self.username, query)
        self.chat_display.insert(tk.END, f"AI: {response}\n\n")
        self.input_entry.delete(0, tk.END)
        self.chat_display.see(tk.END)

    def show(self):
        self.window.deiconify()