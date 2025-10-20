from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()

class FlapCommand(BaseModel):
    value: int

@router.post("/set-flaps")
def set_flaps(cmd: FlapCommand):
    print(f"Setting flaps to {cmd.value}")
    return {"status": "ok", "flaps": cmd.value}