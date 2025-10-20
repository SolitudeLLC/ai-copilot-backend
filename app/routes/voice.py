from fastapi import APIRouter
from app.schemas.voice_schema import VoiceRequest, VoiceResponse
from app.services.voice_service import generate_ai_response

router = APIRouter()

@router.post("/voice", response_model=VoiceResponse)
def handle_voice(request: VoiceRequest):
    result = generate_ai_response(request.text, request.language)
    return VoiceResponse(response=result)
