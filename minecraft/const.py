from pathlib import Path
from const import SERVER_DIR
import subprocess
from functools import partial

START_SCRIPT_FILENAME = 'startserver.sh'
START_SCRIPT_PATH = Path.joinpath(SERVER_DIR, START_SCRIPT_FILENAME)

# subprocess util
mcsub = partial(subprocess.run, capture_output=True, text=True)