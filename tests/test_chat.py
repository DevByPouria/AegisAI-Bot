import pytest

from aegisai.services.chat import build_chat_response


@pytest.mark.parametrize(
    ("user_message", "expected_response"),
    [
        ("سلام", "سلام! 👋"),
        ("خداحافظ", "خداحافظ، روز خوبی داشته باشی. 🌹"),
        ("یک پیام ناشناس", "متوجه منظورت نشدم. 😊"),
        ("  سلام  ", "سلام! 👋"),
    ],
)
def test_chat_responses(
    user_message: str,
    expected_response: str,
):
    response = build_chat_response(user_message)

    assert response == expected_response
