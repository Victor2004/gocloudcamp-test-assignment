# Запуск: python3 -m uvicorn main:app --reload
from fastapi import FastAPI, Request, Body, Depends
from fastapi.responses import HTMLResponse

import schemas
import models
from database import *
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


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
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return f"Config id={id} delete."
