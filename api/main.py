from fastapi import FastAPI
import models
from config import engine
from routes import song
import time

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

## ROUTES ##
app.include_router(song.router)
