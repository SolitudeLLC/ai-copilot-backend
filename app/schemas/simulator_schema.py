# app/schemas/simulator_schema.py

from pydantic import BaseModel

class GearControlRequest(BaseModel):
    down: bool

class GearResponse(BaseModel):
    status: str
