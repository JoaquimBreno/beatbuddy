from fastapi import FastAPI
import models
from config import engine
from tables import song

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
print("Here")
app.include_router(song.router)
