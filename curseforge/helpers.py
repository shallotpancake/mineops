import requests
from pathlib import Path
import curseforge.const as const
from zipfile import ZipFile

def search_mods(search_term):
    url = f"{const.BASE_URL}/mods/search"
    sortField = {"ModLoaderType": "6"}
    params = {"gameId": const.MINECRAFT_ID, "sortField": sortField, "searchFilter": search_term}

    response = const.cfget(url=url, params=params)
    response.raise_for_status()
    mods = response.json()["data"]
    
    return mods

def get_mod_by_id(id):
    url = f"{const.BASE_URL}/mods/{id}"

    response = const.cfget(url=url)
    response.raise_for_status()
    mod = response.json()["data"]
    
    return mod

def search_author(search_term):
    url = f"{const.BASE_URL}/mods/search"
    sortField = {"ModLoaderType": "6"}
    params = {"gameId": const.MINECRAFT_ID, "sortField": sortField, "authorId": search_term}

    response = const.cfget(url=url, params=params)
    response.raise_for_status()
    mods = response.json()["data"]
    
    return mods

def get_mod_id(modpack_name):
    # Search for the modpack to find its ID
    url = f"{const.BASE_URL}/mods/search"
    params = {"gameId": const.MINECRAFT_ID, "searchFilter": modpack_name}  # Game ID 432 is for Minecraft
    response = requests.get(url, headers=const.headers, params=params)
    response.raise_for_status()
    mods = response.json()["data"]
    if not mods:
        raise ValueError(f"Modpack '{modpack_name}' not found.")
    
    return mods[0]["id"]

def get_latest_server_pack_id(mod_id):
    # Get all files for the modpack and filter for the latest server pack
    url = f"{const.BASE_URL}/mods/{mod_id}"
    headers = {"x-api-key": const.API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    mod = response.json()["data"]

    return mod['latestFiles'][0]['serverPackFileId'], mod['dateModified']

def download_server_pack(mod_id, file_id, date_modified):
    # Get the download URL for the server pack
    filename = f"server-{date_modified}.zip"
    file_path = Path.joinpath(const.DOWNLOAD_DIR, filename)
    # Check if file already exists
    if Path(file_path).is_file():
        print(f"Server file is up to date.")
    else:  
      # If it doesn't proceed to download
      url = f"{const.BASE_URL}/mods/{mod_id}/files/{file_id}/download-url"
      headers = {"x-api-key": const.API_KEY}
      response = requests.get(url, headers=headers)
      response.raise_for_status()
      download_url = response.json()["data"]
      print(f"Download URL: {download_url}")
      
      # Download the server pack
      server_pack_response = requests.get(download_url)
      server_pack_response.raise_for_status()
      download_path = Path.joinpath(const.DOWNLOAD_DIR, filename)
      # Write to file
      with open(download_path, "wb") as f:
          f.write(server_pack_response.content)
      print(f"Server pack downloaded to '{download_path}'.")

      return filename
      
def extract_install_server_pack(filename):
    if not const.SERVER_INSTALLED:
      extract_dir = const.SERVER_DIR
      download_dir = const.DOWNLOAD_DIR
      zip_path = Path.joinpath(download_dir, filename)

      # Open the ZIP file
      with ZipFile(zip_path, 'r') as zip_ref:
          # Extract all contents
          zip_ref.extractall(extract_dir)

      print(f"Contents extracted to '{download_dir.absolute()}'")
    else:
        raise NotImplementedError("Server files already exist. Update is not yet implemented")

