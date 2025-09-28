# src/utils/logger.py
import logging
import os
import sys

# Fix for module resolution: Append project root to sys.path
project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def setup_logger():
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fitbit_app.log')
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )