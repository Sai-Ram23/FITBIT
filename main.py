# main.py
import sys
import os
from dotenv import load_dotenv
from src.utils.logger import setup_logger

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from ui.login import LoginWindow
from ui.main import MainWindow

def main():
    load_dotenv()
    setup_logger()
    main_window = None

    def on_login_success(username):
        nonlocal main_window
        if not main_window:
            main_window = MainWindow(username)
        main_window.withdraw()  # Initially hidden
        main_window.show()

    login_window = LoginWindow(on_success_callback=on_login_success)
    login_window.run()

if __name__ == "__main__":
    main()