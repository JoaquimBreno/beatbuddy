
from sqlalchemy.orm import Session
from models import Song
from schema import SongSchema

############ Song ############
def get_songs(db: Session, skipt: int = 0, limit: int = 100):
    return db.query(Song).offset(skipt).limit(limit).all()

def get_songs_by_id(db: Session, Song_id: int):
    return db.query(Song).filter(Song.id_song == Song_id).first()