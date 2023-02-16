import dropbox
import requests
import json
from pathlib import Path
import yaml

DROPBOX_PATH = "dropbox.yaml"
class UploadData:
    def __init__(self, access_token):
        self.dbx = dropbox.Dropbox(oauth2_access_token=access_token["acess_token"], app_key =access_token["app_key"], app_secret = access_token["app_secret"], oauth2_refresh_token = access_token["refresh_token"])
    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        print("Uploading file...")
        with open(file_from, 'rb') as f:
            self.dbx.files_upload(f.read(), file_to)
    def return_link(self, file_to):
        """
            return dropbox link
        """
        print("Generate Link...")
        response =  self.dbx.files_get_temporary_link(file_to)
        return str(response.link)
    
def config_dropbox():
    # Abre o arquivo YAML
    with open(DROPBOX_PATH, 'r') as stream:
        try:
            # Carrega o conteúdo do arquivo como um dicionário Python
            data = yaml.safe_load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)
            return None
    
def dropbox_generator(file_from):
    try:
        access_token = config_dropbox()
        transferData = UploadData(access_token)
        name_to =Path(file_from).name
        file_to = f'/song/{name_to}'  # The full path to upload the file to, including the file name
        # API v2
        transferData.upload_file(file_from, file_to)
        # Return link
        return transferData.return_link(file_to)
    except Exception as err:
        print("Erro Dropbox", err)
        print(err)
        return "erro"
    
print("Insira arquivo: \n")
file = input()
url = dropbox_generator(file)

print(url)

# from modules.shazam import finder, metagen, model


#     # _song = crud.get_songs_no_limit(db,skip,limit)
#     # print(_song)
# song, artist = finder.download_and_find(url)
    
# if(song != None and artist != None):
#     shazam_metadata = {
#         "title": song,
#         "artist": artist
#     }
#     query = song+" "+artist
#     query = query.replace(" ", "%20")
#     spot_metadata = metagen.search_song(query)
#     results = []
#     results = model.main(spot_metadata, "test.json")
#     for key, value in spot_metadata.items():
#         shazam_metadata[key] = value
#     for result in results:
#         print(result)