from functools import partial
from const import CURSEFORGE_SECRET_PATH
import requests

# Get curseforge API token
with open(CURSEFORGE_SECRET_PATH, 'r') as f:
    token = f.read().strip()
if not token:
    raise Exception("Failed to find `.curseforge_api_token` in the current directory.")

# curseforge variables
API_KEY = token
BASE_URL = "https://api.curseforge.com/v1"
MINECRAFT_ID = 432
ATM10_ID = 925200

# Requests variables
headers = {"x-api-key": API_KEY}

cfget = partial(requests.get, headers=headers)



