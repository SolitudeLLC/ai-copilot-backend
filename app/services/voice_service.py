def generate_ai_response(text: str, language: str = "en") -> str:
    # Здесь позже можно использовать OpenAI или любую ML модель
    if "gear" in text.lower():
        return "Lowering the landing gear."
    elif "flaps" in text.lower():
        return "Setting flaps to takeoff position."
    else:
        return f"I received your command: '{text}' in {language}"