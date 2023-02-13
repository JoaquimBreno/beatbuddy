from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
import models
from config import engine
from tables import song

try:
    models.Base.metadata.create_all(bind=engine)
except SQLAlchemyError as err:
    print("error", err.__cause__) 
app = FastAPI()