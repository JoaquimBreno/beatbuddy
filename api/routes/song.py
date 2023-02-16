from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import Response
from modules.shazam import shazam, finder, metagen, model
# from modules.suggester import suggester
import crud


router = APIRouter(
    prefix="/songs", 
    tags=["songs"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_songs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("here")
    _song = crud.get_songs(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_song)

@router.get("/finder")
async def find_song(url: str,db: Session = Depends(get_db)):
    _song = crud.get_songs_no_limit(db)

    song_dicts = [song.__dict__ for song in _song]
    for song_dict in song_dicts:
        song_dict.pop('_sa_instance_state', None)
        
    song, artist = finder.download_and_find(url)
    
    if(song != None and artist != None):
        shazam_metadata = {
            "title": song,
            "artist": artist
        }
        query = song+" "+artist
        query = query.replace(" ", "%20")
        
        spot_metadata = metagen.search_song(query)
        results = []
        results = model.main(spot_metadata, song_dicts)
        
        for key, value in spot_metadata.items():
            shazam_metadata[key] = value

        return Response(status="Ok", code="200", message="Success fetch all data", result=results, original=[spot_metadata])
       
    return Response(status="Ok", code="200", message="Success fetch all data", result={})