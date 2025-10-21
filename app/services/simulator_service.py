import os
import httpx

XPLANE_HOST = os.getenv("XPLANE_HOST", "http://localhost:8086/api/v1")


def handle_xplane_error(response: httpx.Response):
    if response.status_code == 404:
        return {"status": "error", "detail": "Dataref not found"}
    elif response.status_code == 405:
        return {"status": "error", "detail": "Method not allowed"}
    elif response.status_code >= 400:
        return {"status": "error", "detail": f"HTTP error {response.status_code}"}
    return None


async def get_dataref(dataref: str):
    try:
        response = httpx.get(
            f"{XPLANE_HOST}/datarefs?{dataref}",
            timeout=5.0
        )
        error = handle_xplane_error(response)
        if error:
            return error

        values = response.json().get("data", [])
        if not values:
            return {"status": "error", "detail": f"{dataref} not found"}

        return {"status": "ok", "value": values[0].get("value")}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

async def set_dataref(dataref: str, value: float):
    try:
        response = httpx.post(
            f"{XPLANE_HOST}/datarefs",
            json={"dataref": dataref, "value": value},
            timeout=5.0
        )
        error = handle_xplane_error(response)
        if error:
            return error

        return {"status": "ok", "dataref": dataref, "value": value}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


# === HIGH-LEVEL HELPERS ===

async def get_flap_ratio():
    return await get_dataref("sim/cockpit2/controls/flap_ratio")


async def set_flap_ratio(value: float):
    return await set_dataref("sim/cockpit2/controls/flap_ratio", value)


async def get_parking_brake():
    return await get_dataref("sim/flightmodel/controls/parkbrake")


async def set_parking_brake(value: float):
    return await set_dataref("sim/flightmodel/controls/parkbrake", value)


async def get_wing_sweep():
    return await get_dataref("sim/cockpit2/controls/wing_sweep_ratio")


async def set_wing_sweep(value: float):
    return await set_dataref("sim/cockpit2/controls/wing_sweep_ratio", value)
