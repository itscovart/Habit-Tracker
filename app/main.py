from fastapi import FastAPI
from app.db.session import engine, Base
from app.models import habit, run

app = FastAPI(title="Habit & Running Tracker")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API running"}