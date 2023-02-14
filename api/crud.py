
from sqlalchemy.orm import Session
from models import Songs
from schema import SongsSchema

############ Song ############
def get_songs(db: Session, skipt: int = 0, limit: int = 100):
    return db.query(Songs).offset(skipt).limit(limit).all()

def get_songs_no_limit(db: Session, skipt: int = 0, limit: int = 1000):
    return db.query(Songs).offset(skipt).limit(limit).all()

def get_songs_by_id(db: Session, Song_id: int):
    return db.query(Songs).filter(Songs.id_song == Song_id).first()
