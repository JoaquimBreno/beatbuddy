from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base  = declarative_base()

class Songs(Base):
    __tablename__ = 'songs_prod'
    track_name= Column(Integer, primary_key=True, index=True, autoincrement=True)
    artist_name = Column(String)
    genre = Column(String)
    key = Column(String)
    mode = Column(String)
    tempo = Column(String)
    duration = Column(String)
    time_signature = Column(String)
    