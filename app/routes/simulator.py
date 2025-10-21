from fastapi import APIRouter, Query
from app.services import simulator_service

router = APIRouter(prefix="/simulator", tags=["Simulator"])


@router.get("/flaps")
async def get_flaps():
    return await simulator_service.get_flap_ratio()

@router.put("/flaps")
async def set_flaps(value: float = Query(..., ge=0.0, le=1.0)):
    return await simulator_service.set_flap_ratio(value)


@router.get("/parking_brake")
async def get_parking_brake():
    return await simulator_service.get_parking_brake_ratio()


@router.post("/parking_brake")
async def post_parking_brake(value: float = Query(..., ge=0.0, le=1.0)):
    return await simulator_service.set_parking_brake_ratio(value)


@router.get("/gear")
async def get_gear_handle():
    return await simulator_service.get_gear_handle_down()


@router.post("/gear")
async def post_gear_handle(value: float = Query(..., ge=0.0, le=1.0)):
    return await simulator_service.set_gear_handle_down(value)
