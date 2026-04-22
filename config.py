from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    app_env: str = os.getenv("APP_ENV", "local")
    app_host: str = os.getenv("APP_HOST", "0.0.0.0")
    app_port: int = int(os.getenv("APP_PORT", "8000"))
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_webhook_url: str = os.getenv("TELEGRAM_WEBHOOK_URL", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    database_path: str = os.getenv("DATABASE_PATH", "./database.db")
    data_dir: str = os.getenv("DATA_DIR", "./data_raw")
    methods_dir: str = os.getenv("METHODS_DIR", "./app/methods")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    @property
    def db_file(self) -> Path:
        return Path(self.database_path)

settings = Settings()
