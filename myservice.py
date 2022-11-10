import schemas
import models
from database import *
from sqlalchemy.orm import Session
from fastapi import Depends

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def get_service_configs(session = Session(bind=engine)):
    all_configs = session.query(models.MyserviceDB).all()
    return all_configs

settings = {"service_id": None}

def get_congif(id=None):
    global settings
    if id:
        settings["service_id"] = id
        print("Config update!")
    return settings["service_id"]
