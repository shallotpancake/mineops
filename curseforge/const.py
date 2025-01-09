from functools import partial
import requests

# Get curseforge API token
with open('./.curseforge_api_token') as f:
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



