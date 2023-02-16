import pandas as pd
import numpy as np
import json
import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 
from sklearn.preprocessing import MinMaxScaler

def load_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
    return data

def next_song_pratice (song, banco):
    #  banco e new song data em json
    # import data from database  
    data = banco
  
    df = pd.DataFrame(data).fillna("")
    df['id'] = df['track_name'] + " ( " + df['artist_name'] + " )"
    df = df.set_index('id').fillna("").drop(columns=["track_name", "artist_name"], axis= 1)
    for i , r in df.iterrows():
        if "pop" in df.loc[ i, "genre"]: 
            df.loc[ i, "genre"] = "pop"
        elif any(substring in df.loc[ i, "genre"] for substring in ["hip hop", "rap", "r&b", "trap"]):
            df.loc[ i, "genre"] = "hip hop"
        elif "country" in df.loc[ i, "genre"]: 
            df.loc[ i, "genre"] = "country"
        elif any(substring in df.loc[ i, "genre"] for substring in ["rock", "metal"]):
            df.loc[ i, "genre"] = "rock"
        else: 
            df.loc[ i, "genre"] = "other"
            
    df["tempo"] = pd.to_numeric(df["tempo"])
    df["key"] = pd.to_numeric(df["key"])
    df["mode"] = pd.to_numeric(df["mode"])
    df["duration"] = pd.to_numeric(df["duration"])
    df["time_signature"] = pd.to_numeric(df["time_signature"])
    
    # import new song 
    song = [song]
    new_song = pd.DataFrame(song).fillna("")
    
    if "pop" in str(new_song.loc[0,"genre"]): 
        new_song.loc[0,"genre"] = "pop"
    elif  any(substring in str(new_song.loc[0,"genre"]) for substring in ["hip hop", "rap", "r&b", "trap"]): 
        new_song.loc[0,"genre"] = "hip hop"
    elif "country" in str(new_song.loc[0,"genre"]): 
        new_song.loc[0,"genre"] = "country"
    elif any(substring in str(new_song.loc[0,"genre"]) for substring in ["rock", "metal"]):
        new_song.loc[0,"genre"] = "rock"
    else: 
        new_song.loc[0,"genre"] = "other"
        
    # filter and normalize database

    song_genre = new_song.loc[0,"genre"]
  
    col_to_use = [ "tempo", "key", "mode", "duration", "time_signature"]
    base = df[df["genre"] == song_genre].loc[:, col_to_use ]
        
    scaler = MinMaxScaler(feature_range = (0,1))
    scaled_data = scaler.fit_transform(base)
    base_norm = pd.DataFrame(scaled_data, columns=col_to_use, index=base.index)
    
    # model
    k = 4
    kmeans = KMeans(n_clusters=k, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0).fit(base_norm)
    base_norm["group"] = kmeans.labels_ 
    
    # prepare song to predict
    def normalizador (value, column):
        value_norm = (float(value) - float(base[column].min()) ) / (float(base[column].max()) - float(base[column].min()))
        return value_norm

    list_columns = base.columns
    new_song_to_predict = new_song.loc[0 , col_to_use]
    new_song_norm = []
    for index, value in enumerate(new_song_to_predict):
        new_song_norm.append( normalizador(value, list_columns[index] ))
    
    #prediction
    target_group = kmeans.predict([new_song_norm])[0]
    sugestions = base_norm[base_norm["group"] == target_group]
    sugestions = sugestions.index.tolist()
    return sugestions

def main(new_song, banco):
    
    i = time.time()
    musicas = next_song_pratice(new_song, banco)
    e = time.time()
    
    print("Time: " ,e - i)  
    
    return musicas
 
