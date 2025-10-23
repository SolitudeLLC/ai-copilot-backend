import logging
from fastapi import FastAPI
from app.routes import voice, simulator

app = FastAPI()

app.include_router(voice.router)
app.include_router(simulator.router)

logging.basicConfig(level=logging.DEBUG)

# Enable httpx debug logs
logging.getLogger("httpx").setLevel(logging.DEBUG)
logging.getLogger("httpcore").setLevel(logging.DEBUG)
