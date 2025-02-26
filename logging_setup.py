# logging_setup.py
import logging
from io import StringIO

def setup_logging():
    """
    Set up logging to capture logs in a StringIO buffer.

    Returns:
        tuple: A tuple containing the logger and the log stream.
    """
    log_stream = StringIO()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=log_stream
    )
    logger = logging.getLogger(__name__)
    return logger, log_stream