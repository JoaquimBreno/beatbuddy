from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base  = declarative_base()

class Songs(Base):
    __tablename__ = 'songs'
    id_song= Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    artist = Column(String)