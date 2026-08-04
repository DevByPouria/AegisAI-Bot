def build_chat_response(message: str) -> str:
    message = message.strip()
    if message == "سلام":
        return "سلام! 👋"

    elif message == "خداحافظ":
        return "خداحافظ، روز خوبی داشته باشی. 🌹"

    else:
        return "متوجه منظورت نشدم. 😊"
