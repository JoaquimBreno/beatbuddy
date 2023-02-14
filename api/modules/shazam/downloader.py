import dropbox
import requests
import json
import re
from pathlib import Path
import hashlib
import yaml

FOLDER = "data"
DROPBOX_PATH = "dropbox.yaml"

class DownloadData:
    def __init__(self, access_token):
        self.dbx = dropbox.Dropbox(oauth2_access_token=access_token["acess_token"], app_key =access_token["app_key"], app_secret = access_token["app_secret"], oauth2_refresh_token = access_token["refresh_token"])
    #download file from dropbox
    def download_file(self, dropbox_file_path, local_file_path):
        try:
            # with open(local_file_path, 'wb') as f:
            response = requests.get(dropbox_file_path)
            content_disposition = response.headers.get('Content-Disposition')
            try:
                if content_disposition:
                    match = re.search('filename="(.+)"', content_disposition)
                    if match:
                        filename = match.group(1)
            except:
                # some treatement for the case when the filename is not in the Content-Disposition header
                content_type = response.headers.get('Content-Type')
                if content_type:
                    ext = content_type.split('/')[-1]
                    if ext:
                        filename = hashlib.sha256(response.content).hexdigest() + "." + ext
                else:
                    filename = hashlib.sha256(response.content).hexdigest() + ".mp3"
            with open(filename, 'wb') as f:
                f.write(response.content)
            return filename
        except Exception as e:
            print('Error downloading file from Dropbox: ' + str(e))
            return None
    
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
    
def dropbox_downloader(download_path):
    try:
        access_token = config_dropbox()
        transferData = DownloadData(access_token)
        file_to = FOLDER
        filename = transferData.download_file(download_path, file_to)
        return filename
    except Exception as err:
        print("Erro Dropbox", err)
        print(err)
        return None
    