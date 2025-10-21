from fastapi import FastAPI
from app.routes import voice, simulator

app = FastAPI()

app.include_router(voice.router)
app.include_router(simulator.router)
