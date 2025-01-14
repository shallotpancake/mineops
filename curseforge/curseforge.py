
import curseforge.helpers as cf

def download_latest_atm10():
    # attempts to download latest server pack
    # if the latest is already downloaded, skip

    print(f"Attempting to download ATM10 server pack...")
    mod_id = 925200 #ATM10 ID
    download_url, file_id = cf.get_latest_server_file_url(mod_id)
    filename = cf.download_server_pack(download_url, file_id)
    print(f"filename: {filename}")
    cf.extract_server_pack(filename)


