import os

# COMMON
APP_VERSION = 'v1.0.0'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH_SCAN_LOG_FILE = os.path.join(BASE_DIR, "logs", "scan.log")

# GUI APP
WINDOW_TITLE = 'Folder Size Scanner'
WINDOW_SIZE = '600x400'

# CLI MESSAGES
MESSAGE_USE_GUI = 'Would you like to use the graphical interface (y/N)? '
MESSAGE_GET_INPUT_PATH = 'Enter the folder path to start the scan: '
MESSAGE_GET_RELEVANT_SIZE = 'Enter the relevant size for logging (e.g., 1GB, 500MB, 100KB) or press Enter to skip: '
