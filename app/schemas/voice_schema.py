from pydantic import BaseModel

class VoiceRequest(BaseModel):
    text: str
    language: str = "en"

class VoiceResponse(BaseModel):
    response: str