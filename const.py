from pathlib import Path

# file variables
SERVER_DIR = Path('server')
DOWNLOAD_DIR = Path('downloads')

# Make these paths if they don't exist
Path.mkdir(SERVER_DIR, exist_ok=True)
Path.mkdir(DOWNLOAD_DIR, exist_ok=True)

# Check if server files exist in SERVER_DIR
SERVER_INSTALLED = any(SERVER_DIR.iterdir())