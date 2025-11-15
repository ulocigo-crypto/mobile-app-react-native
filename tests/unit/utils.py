import re
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

def validate_email(email):
    """
    Validate an email address.
    
    Args:
        email (str): Email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def get_current_directory():
    """
    Get the current working directory.
    
    Returns:
        str: Current working directory.
    """
    return os.getcwd()

def get_project_root():
    """
    Get the root directory of the project.
    
    Returns:
        str: Project root directory.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_app_data_directory():
    """
    Get the directory where app data is stored.
    
    Returns:
        str: App data directory.
    """
    return os.path.join(get_project_root(), 'app_data')

def get_logs_directory():
    """
    Get the directory where logs are stored.
    
    Returns:
        str: Logs directory.
    """
    return os.path.join(get_project_root(), 'logs')