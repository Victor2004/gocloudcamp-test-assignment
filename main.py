# Запуск: python3 -m uvicorn main:app --reload
from fastapi import FastAPI, Request, Body, Depends
from fastapi.responses import HTMLResponse

import schemas
import models
from database import *
from sqlalchemy.orm import Session

import myservice

app = FastAPI()

Base.metadata.create_all(engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# def create_default_config(session = Depends(get_session)):;
#     item = models.Item(service = item.service, data = item.data);
#     session.add(item);
#     session.commit();
#     session.refresh(item);
# create_default_config();

@app.get("/help")
def help():
    return "Hello world!"

@app.get("/")
def get_item(id: str, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

@app.post("/")
def add_item(item: schemas.Item, session = Depends(get_session)):
    item = models.Item(service = item.service, data = item.data)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.put("/{id}")
def update_item(id:int, item:schemas.Item, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject

@app.delete("/{id}")
def delete_item(id:int, session = Depends(get_session)):
    if myservice.use_config() == id:
        return "You can not delete the config used by the service."
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return f"Config id={id} delete."

@app.get("/service")
def get_service_config(session: Session = Depends(get_session)):
    item = None
    if myservice.use_config():
        item = session.query(models.Item).get(myservice.use_config())
    return item

@app.put("/service/{id}")
def update_service_config(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(myservice.use_config(id))
    return "Config update!", item