from pydantic import BaseModel, Field
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')

############ Song ############
class SongSchema(BaseModel):
    id_song = int
    title = str
    artist = str

    class Config:
        orm_mode = True

class RequestSong(BaseModel):
    parameter: SongSchema = Field(...)
    
class Response(GenericModel, Generic[T]):
    code:str
    status: str
    message: str
    result: Optional[T]