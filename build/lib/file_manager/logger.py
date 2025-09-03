# Logging decorators 

import functools
import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "actions.log")
LOG_FILE = os.path.abspath(LOG_FILE)

def log_action(func):
    """Decorator to log function calls with timestamp and arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {func.__name__} args={args[1:]}, kwargs={kwargs}, result={result}\n"

        with open(LOG_FILE, "a") as log:
            log.write(log_entry)

        return result
    return wrapper
