from fastapi import FastAPI

app = FastAPI(title="Habit & Running Tracker")

@app.get("/")
def root():
    return {"message": "API running"}