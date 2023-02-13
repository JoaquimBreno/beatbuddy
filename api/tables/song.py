from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import SongsSchema, Response, RequestSongs

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
    _song = crud.get_songs(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_song)