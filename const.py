from pathlib import Path

# Path variables
SERVER_DIR = Path('server')
DOWNLOAD_DIR = Path('downloads')
LOG_DIR = Path('logs')

# File variables
TEST_LOG_FILE_PATH = Path.joinpath(LOG_DIR, 'test_output.log').absolute()

# secrets
CURSEFORGE_SECRET_PATH = Path('.curseforge_api_token')

# Make these paths if they don't exist
Path.mkdir(SERVER_DIR, exist_ok=True)
Path.mkdir(DOWNLOAD_DIR, exist_ok=True)
Path.mkdir(LOG_DIR, exist_ok=True)

# Check if server files exist in SERVER_DIR
SERVER_INSTALLED = any(SERVER_DIR.iterdir())
