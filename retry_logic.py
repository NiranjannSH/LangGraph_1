# retry_logic.py
import time
import logging


def retry(max_retries=3, delay=1):
    """Decorator to retry a function if it fails."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.error(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            logging.error(f"Max retries ({max_retries}) exceeded")
            return {"status": "error", "message": "Max retries exceeded"}
        return wrapper
    return decorator
