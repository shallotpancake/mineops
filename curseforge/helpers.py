import requests
from pathlib import Path
import curseforge.const as cfconst
try:
    import const
except:
    from .. import const
from zipfile import ZipFile
import os
import shutil

def get_mod_by_id(id):
    print("Getting mod via id...")
    url = f"{cfconst.BASE_URL}/mods/{id}"

    response = cfconst.cfget(url=url)
    response.raise_for_status()
    mod = response.json()["data"]
    
    return mod

def get_mod_id(modpack_name):
    # Search for the modpack to find its ID
    url = f"{cfconst.BASE_URL}/mods/search"
    params = {"gameId": cfconst.MINECRAFT_ID, "searchFilter": modpack_name}  # Game ID 432 is for Minecraft
    response = requests.get(url, headers=cfconst.headers, params=params)
    response.raise_for_status()
    mods = response.json()["data"]
    if not mods:
        raise ValueError(f"Modpack '{modpack_name}' not found.")
    
    return mods[0]["id"]

def get_latest_server_pack_id(mod_id):
    # Get all files for the modpack and filter for the latest server pack
    print("Getting latest server pack id...")
    url = f"{cfconst.BASE_URL}/mods/{mod_id}"
    response = cfconst.cfget(url)
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
      url = f"{cfconst.BASE_URL}/mods/{mod_id}/files/{file_id}/download-url"
      headers = {"x-api-key": cfconst.API_KEY}
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
      
def extract_server_pack(filename):
    if const.SERVER_INSTALLED:
        print("Server files already exist. Update is not yet implemented")  
        return 1
    
    extract_dir = const.SERVER_DIR
    download_dir = const.DOWNLOAD_DIR
    zip_path = Path.joinpath(download_dir, filename)
    # List the top-level contents of the extracted directory
    top_level_items = os.listdir(extract_dir)

    if len(top_level_items) == 1:
        single_item = os.path.join(extract_dir, top_level_items[0])
        if os.path.isdir(single_item):
            # Move all contents of the subdirectory to the parent directory
            for item in os.listdir(single_item):
                shutil.move(os.path.join(single_item, item), extract_dir)
            
            # Remove the now-empty subdirectory
            os.rmdir(single_item)
            print(f"Moved contents of {single_item} to {extract_dir} and removed the empty folder.")
    # Open the ZIP file
    with ZipFile(zip_path, 'r') as zip_ref:
        # Extract all contents
        zip_ref.extractall(extract_dir)
    print(f"Contents extracted to '{download_dir.absolute()}'")


