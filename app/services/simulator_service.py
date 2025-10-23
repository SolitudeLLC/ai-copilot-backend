import os
import httpx

XPLANE_HOST = os.getenv("XPLANE_HOST", "http://localhost:8086/api/v2")


def handle_xplane_error(response: httpx.Response):
    if response.status_code == 404:
        return {"status": "error", "detail": "Dataref not found"}
    elif response.status_code == 405:
        return {"status": "error", "detail": "Method not allowed"}
    elif response.status_code >= 400:
        return {"status": "error", "detail": f"HTTP error {response.status_code}"}
    return None


async def get_datarefByName(dataref: str):
    try:
        response = httpx.get(
            f"{XPLANE_HOST}/datarefs?{dataref}",
            timeout=5.0
        )
        error = handle_xplane_error(response)
        if error:
            return error

        values = response.json().get("data", [])
        # if not values:
        #     return {"status": "error", "detail": f"{dataref} not found"}

        # return {"status": "ok", "value": values[0].get("value")}

        found = next((item for item in values if item["name"] == dataref), None)
        return {"status": "ok", "value": found}

    except Exception as e:
        return {"status": "error", "detail": str(e)}

async def set_dataref(id: str, value: float):
    try:
        response = httpx.patch(
            f"{XPLANE_HOST}/datarefs/{id}/value",
            json={ "data": value },
            timeout=5.0
        )
        error = handle_xplane_error(response)
        if error:
            return error

        return {"status": "ok", "id": id, "response": response}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


# === HIGH-LEVEL HELPERS ===


async def get_flap_ratio_dataref_value():
    result = await get_datarefByName("sim/cockpit2/controls/flap_ratio") 
    value = result["value"]
    return value

async def get_flap_ratio():
    dataref = await get_flap_ratio_dataref_value()
    dataref_id = dataref["id"]
    response = httpx.get(
            f"{XPLANE_HOST}/datarefs/{dataref_id}/value",
            timeout=5.0
        )
    error = handle_xplane_error(response)
    return response.text


async def set_flap_ratio(value: float):
    dataref = await get_flap_ratio_dataref_value()
    dataref_id = dataref["id"]
    return await set_dataref(dataref_id, value)


async def get_parking_brake():
    return await get_datarefByName("sim/flightmodel/controls/parkbrake")


async def set_parking_brake(value: float):
    return await set_dataref("sim/flightmodel/controls/parkbrake", value)


