from ShazamAPI import Shazam
from modules.shazam import downloader

def song_finder_shazam(audio_file):
    try: 
        mp3_file_content_to_recognize = open(audio_file, 'rb').read()

        shazam = Shazam(mp3_file_content_to_recognize)

        recognize_generator = shazam.recognizeSong()

        result = next(recognize_generator)

        if(len(result[1]["matches"]) == 0):
            raise("There is no match for this song")
        song = result[1]["track"]["title"]
        artist = result[1]["track"]["subtitle"]
    
        return song, artist
    
    except Exception as err:
        print(err)
        return None, None

def download_and_find(url):
    try:
        filename = downloader.dropbox_downloader(url)
    except Exception as err:
        print(err)
    else:
        return song_finder_shazam(filename)
    