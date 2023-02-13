from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

import sqlalchemy


#DATABASE_URI = "postgresql://boadlfsiavrxeb:e743d7b2ab5b25f237e8326cecf8e27b487686821f168ea7fac6ebed4bd4deb4@ec2-44-207-133-100.compute-1.amazonaws.com:5432/da9obqdvpm8te8"
#engine = connect_with_connector()
DATABASE_URI = "postgresql://postgres:recomenda@127.0.0.1:5432/database_test"
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()