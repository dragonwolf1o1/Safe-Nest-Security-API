import logging

# Create a custom logger
logger = logging.getLogger("safenest_logger")
logger.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add handler to logger
if not logger.hasHandlers():
    logger.addHandler(console_handler)
