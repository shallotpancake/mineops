
import curseforge.helpers as cf

def download_latest_atm10():
    mod_id = 925200 #ATM10 ID
    file_id = cf.get_latest_server_pack_id(mod_id)
    print(f"mod_id: {mod_id}\nserver file id: {file_id}")
    cf.download_server_pack(mod_id, file_id)


