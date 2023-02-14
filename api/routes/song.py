from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import Response
from modules.shazam import shazam, finder
from modules.suggester import suggester
from modules import uploader
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
async def find_song(url: str, db: Session = Depends(get_db)):
    song, artist = finder.download_and_find(url)
    if(song != None and artist != None):
        shazam_metadata = {
            "title": song,
            "artist": artist
        }
        return Response(status="Ok", code="200", message="Success fetch all data", result=shazam_metadata)
       
    return Response(status="Ok", code="200", message="Success fetch all data", result={})