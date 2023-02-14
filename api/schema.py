from pydantic import BaseModel, Field
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')

############ Song ############
class SongsSchema(BaseModel):
    track_name = int
    artist_name = str
    genre = str
    key = str
    mode = str
    tempo = str
    duration = str
    time_signature = str

    class Config:
        orm_mode = True

class RequestSongs(BaseModel):
    parameter: SongsSchema = Field(...)
    
class Response(GenericModel, Generic[T]):
    code:str
    status: str
    message: str
    result: Optional[T]