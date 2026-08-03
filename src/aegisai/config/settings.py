import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    bot_token: str
    debug: bool


settings = Settings(
    bot_token=os.getenv("BOT_TOKEN", ""),
    debug=os.getenv("DEBUG", "False").lower() == "true",
)
