import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import musicbrainzngs
import json
from Levenshtein import distance
client_id = "df88778eb91346e3bd437b2ce1c28197"
client_secret = "2ce8feb7c95c465f835219f5a2a41372"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# playlist_URI="3IsxzDS04BvejFJcQ0iVyW"
# track_uris = [x["track"]["uri"] for x in spotify.playlist_tracks(playlist_URI)["items"]]
def get_songs_att(track_uri):
    jsons = {}

    features = spotify.audio_features(track_uri)[0]
    jsons["key"] = features["key"]
    jsons["mode"] = features["mode"]
    jsons["tempo"]=features["tempo"]
    jsons["duration"]=features["duration_ms"]
    jsons["time_signature"]=features["time_signature"]
 
    return jsons

# def search_irsc(artist_name, track_name):
#     musicbrainzngs.auth("joaquimbr", "musicbrainz123")
#     musicbrainzngs.set_useragent("Exemplo de busca IRSC", "0.1", "contatojoaquim.breno@gmail.com")

#     result = musicbrainzngs.search_releases(artist=artist_name, release=track_name)
#     # print(result["release-list"][0])
#     if result["release-list"]:
#         release_id = result["release-list"][0]
#         print(release_id)
#         #res = musicbrainzngs.get_release_by_id(label=result["release-list"][0]["label-info-list"][0]["label"]["id"])
#         #print(res)
#         #release_info = musicbrainzngs.get_release_group_by_id(release_id, includes=["recordings+isrcs"])
#         #print(release_info)
#         # isrcs = release_info["release"]["isrc-list"]
#         # if isrcs:
#         #     print("IRSCs encontrados:")
#         #     for isrc in isrcs:
#         #         print(isrc)
#         # else:
#         #     print("Não foram encontrados IRSCs para a música.")
#     else:
#         print("Nenhum lançamento encontrado para a música.")
        
        
def search_song(query):
    test = spotify.search(query, type='track', limit=20)["tracks"]["items"]
    artist_uri=test[0]["album"]["artists"][0]["uri"]
    artist_info = spotify.artist(artist_uri)
    artist_genres = artist_info["genres"]
    if(len(artist_genres)):
        artist_genres[0]
    else:
        artist_genres = ""
    similaridade_ant=0
    index = 0
    jsons = []
    for id, item in enumerate(test):
        attributes = {}
        frase1= item["name"] + item["artists"][0]["name"] 
        frase2= query
        similaridade = 1 - (distance(frase1, frase2) / max(len(frase1), len(frase2)))
        if similaridade > similaridade_ant:
            index = id
        try:
            attributes = get_songs_att(item["uri"])
        except Exception as err:
            print(err)
        if(attributes != {}):
            all_json = attributes
        else:
            all_json = {}
        all_json["artist"] = item["artists"][0]["name"]
        all_json["track_name"] =item["name"]
        all_json["uri"] = item["uri"]
        jsons.append(all_json)
        similaridade_ant = similaridade
    value = {}
    try:
        jsons[index]["genre"] = artist_genres
        value=jsons[index]
    except Exception as err:
        print(err)

    return value

