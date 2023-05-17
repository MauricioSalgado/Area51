from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field

from database import engine, SessionLocal
from sqlalchemy.orm import Session

from routers import router_general
from routers import router_watches
from models import model_watch
import database

app = FastAPI()

app.include_router(router_watches.router)


model_watch.Base.metadata.create_all(bind=engine)




class Watch(BaseModel):
    brand: str = Field(min_length=1)
    model: str = Field(min_length=1)
    year: int = Field(gt=1800)
    price: int = Field(gt=1)



@app.get("/watches/get")
def read_api(db: Session = Depends(database.get_db)):
    return db.query(model_watch.Watch).all()


@app.post("/watches/add")
def add_watch(watch: Watch, db: Session = Depends(database.get_db)):
    
    new_watch = model_watch.Watch()
    new_watch.brand = watch.brand
    new_watch.model = watch.model
    new_watch.year = watch.year
    new_watch.price = watch.price

    db.add(new_watch)
    db.commit()

    return watch