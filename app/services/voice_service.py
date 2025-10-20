# app/services/voice_service.py

from app.services.ai_service import ask_openai

def generate_ai_response(text: str, language: str) -> str:
    return ask_openai(text, language)
