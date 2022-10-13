import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASSWORD")
HOSTNAME = os.environ.get("DB_HOSTNAME")
PORT = os.environ.get("DB_PORT")
SCHEMA_NAME = os.environ.get("DB_SCHEMA_NAME")

engine = create_engine(
    url=f"mysql://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{SCHEMA_NAME}"
)
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
