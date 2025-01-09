
import curseforge.helpers as cf

def download_latest_atm10():
    # attempts to download latest server pack
    # if the latest is already downloaded, skip
    mod_id = 925200 #ATM10 ID
    file_id, date_modified = cf.get_latest_server_pack_id(mod_id)
    print(f"mod_id: {mod_id}\nserver file id: {file_id}\nlast modified: {date_modified}")
    cf.download_server_pack(mod_id, file_id, date_modified)


