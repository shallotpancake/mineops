import requests
from functools import partial

with open('./.curseforge_api_token') as f:
    token = f.read().strip()
if not token:
    raise "Failed to find `.curseforge_api_token` in the current directory."

API_KEY = token
BASE_URL = "https://api.curseforge.com/v1"
MINECRAFT_ID = 432

headers = {"x-api-key": API_KEY}

cfget = partial(requests.get, headers=headers)

def search_mods(search_term):
    url = f"{BASE_URL}/mods/search"
    sortField = {"ModLoaderType": "6"}
    params = {"gameId": MINECRAFT_ID, "sortField": sortField, "searchFilter": search_term}

    response = cfget(url=url, params=params)
    response.raise_for_status()
    mods = response.json()["data"]
    
    return mods

def get_mod_by_id(id):
    url = f"{BASE_URL}/mods/{id}"

    response = cfget(url=url)
    response.raise_for_status()
    mod = response.json()["data"]
    
    return mod

def search_author(search_term):
    url = f"{BASE_URL}/mods/search"
    sortField = {"ModLoaderType": "6"}
    params = {"gameId": MINECRAFT_ID, "sortField": sortField, "authorId": search_term}

    response = cfget(url=url, params=params)
    response.raise_for_status()
    mods = response.json()["data"]
    
    return mods


def get_mod_id(modpack_name):
    # Search for the modpack to find its ID
    url = f"{BASE_URL}/mods/search"
    params = {"gameId": MINECRAFT_ID, "searchFilter": modpack_name}  # Game ID 432 is for Minecraft
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    mods = response.json()["data"]
    if not mods:
        raise ValueError(f"Modpack '{modpack_name}' not found.")
    return mods[0]["id"]

def get_latest_server_pack_id(mod_id):
    # Get all files for the modpack and filter for the latest server pack
    url = f"{BASE_URL}/mods/{mod_id}"
    headers = {"x-api-key": API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    mod = response.json()["data"]
    return mod['latestFiles'][0]['serverPackFileId'] 
    raise ValueError("No server pack found for this modpack.")

def download_server_pack(mod_id, file_id):
    # Get the download URL for the server pack

    url = f"{BASE_URL}/mods/{mod_id}/files/{file_id}/download-url"
    headers = {"x-api-key": API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    download_url = response.json()["data"]
    print(f"Download URL: {download_url}")
    
    # Download the server pack
    server_pack_response = requests.get(download_url)
    server_pack_response.raise_for_status()
    with open("server-pack.zip", "wb") as f:
        f.write(server_pack_response.content)
    print("Server pack downloaded as 'server-pack.zip'.")

def download_latest_atm10():
    mod_id = 925200 #ATM10 ID
    file_id = get_latest_server_pack_id(mod_id)
    print(f"mod_id: {mod_id}\nserver file id: {file_id}")
    download_server_pack(mod_id, file_id)


