import requests
from pathlib import Path
import curseforge.const as cfconst
import const
from zipfile import ZipFile
import shutil


def is_release_with_server(file: dict):
    if  file.get('isServerPack', False):
        print("File is a server pack.")
        return False
    if not file.get('serverPackFileId', False):
        print("File does not have a server pack.")
        return False
    if not file.get('downloadUrl', False):
        print("File has no download url.")

    return True

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

def get_mod_by_id(id):
    print("Getting mod via id...")
    url = f"{cfconst.BASE_URL}/mods/{id}"

    response = cfconst.cfget(url=url)
    response.raise_for_status()
    mod = response.json()["data"]
    
    return mod

def get_latest_server_file_url(mod_id: int) -> tuple[str, str]:
    """Gets file info for the latest modpack server

    Args:
        mod_id (int): Curseforge ID for modpack

    Returns:
        tuple[str, str]: download URL, file name
    """
    url = f"{cfconst.BASE_URL}/mods/{mod_id}/files/"
    response = cfconst.cfget(url=url)
    files = response.json()['data']
    for file in files:
        if is_release_with_server(file):
            print(f"Latest full release: {file.get('displayName')}\nDownloads: {file.get('downloadCount')}")
            server_file_id = file.get('serverPackFileId')
            full_download_url = f"{url}{server_file_id}/download-url/"
            return full_download_url, file.get('fileName').replace(" ", "")

    raise Exception("No valid files found")

def download_server_pack(download_url, file_id):
    # Check if file already exists
    
    if Path(Path.joinpath(const.DOWNLOAD_DIR, file_id)).is_file():
        print(f"Server file is up to date.")
    else:  
      # If it doesn't proceed to download
      download_path = Path.joinpath(const.DOWNLOAD_DIR, file_id)
      server_pack_response = cfconst.cfget(download_url)
      server_pack_response.raise_for_status()
      download_file(server_pack_response.json()["data"], download_path)
      print(f"Server pack downloaded to '{download_path}'.")

    return file_id

def download_file(url, local_filename):
    # Send a GET request to the URL
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Raise an error for bad status codes
        # Open a local file with write-binary mode
        with open(local_filename, 'wb') as file:
            # Write the content to the local file in chunks
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    return local_filename

def extract_server_pack(filename):
    if const.SERVER_INSTALLED:
        print("Server files already exist. Update is not yet implemented")  
        return 1

    extract_dir = const.SERVER_DIR
    download_dir = const.DOWNLOAD_DIR
    zip_path = Path.joinpath(download_dir, filename)
    
    # Extract all files
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    # Get the list of items in the extract_dir directory
    extracted_items = list(extract_dir.iterdir())
    
    # Check if there's only one item, and if it's a directory
    if len(extracted_items) == 1 and extracted_items[0].is_dir():
        subdir = extracted_items[0]
        
        # Move all files from the subdirectory to the parent directory
        for item in subdir.iterdir():
            shutil.move(str(item), extract_dir / item.name)
        
        # Remove the now-empty subdirectory
        subdir.rmdir()
        print(f"Moved files from subdirectory '{subdir}' to '{extract_dir}' and removed the subdirectory.")
    else:
        print("Extracted contents are not in a single subdirectory.")


