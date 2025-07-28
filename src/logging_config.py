import logging
import os
import sys
from logging.handlers import RotatingFileHandler

def configure_logging():
    # Create a logger object
    logger = logging.getLogger('gen-1f3da508-7266-429e-8cfc-5c3916bcf455')
    logger.setLevel(logging.DEBUG)  # Set the logging level to debug

    # Define format for logging
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create console handler and set level to debug
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Create file handler which logs even debug messages
    log_file_path = os.path.join(os.getcwd(), 'logs', 'application.log')
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    file_handler = RotatingFileHandler(log_file_path, maxBytes=1024*1024*5, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Add logging to Flask app
    from flask import Flask
    app = Flask(__name__)
    app.logger.addHandler(console_handler)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)

    return app, logger

# Configure logging when module is imported
app, logger = configure_logging()