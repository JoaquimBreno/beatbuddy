from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import SongSchema, Response, RequestSong

import crud

router = APIRouter(
    prefix="/song", 
    tags=["song"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_song(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _song = crud.get_song(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_song)