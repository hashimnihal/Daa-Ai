from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Smart Route Planner")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Smart Route Planner Backend Running"}