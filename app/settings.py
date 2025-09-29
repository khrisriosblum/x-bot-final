
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # -------- Core bot config --------
    # Si usas plan Starter con disco: /data/tracks.xlsx
    # Si usas Free sin disco:       /app/data/tracks.xlsx
    EXCEL_PATH: str = Field(default="/data/tracks.xlsx")
    TIMEZONE: str = Field(default="Europe/Madrid")
    POST_TIMES: str = Field(default="10:00,13:00,16:00,19:00,22:00")
    JITTER_MINUTES: int = Field(default=15)
    SLEEP_BEFORE_PUBLISH: int = Field(default=15)
    DEDUP_DAYS: int = Field(default=70)
    RECENT_DAYS: int = Field(default=2)
    SOUND_CLOUD_EVERY_N_DAYS: int = Field(default=3)
    SPOTIFY_TOPS_EVERY_N_DAYS: int = Field(default=10)
    START_DATE: str = Field(default="2025-01-01")

    # -------- X (Twitter) credentials --------
    X_API_KEY: str = Field(default="")
    X_API_SECRET: str = Field(default="")
    X_ACCESS_TOKEN: str = Field(default="")
    X_ACCESS_SECRET: str = Field(default="")
    # Opcional, solo para construir URL legible del tweet si tenemos el id
    X_USERNAME: str = Field(default="")

    # -------- Runtime --------
    # Si usas Starter con disco: /data/bot.db
    # Si usas Free sin disco:    /app/bot.db
    DRY_RUN: bool = Field(default=True)
    DB_PATH: str = Field(default="/data/bot.db")
    PORT: int = Field(default=8000)

    # -------- Email (SMTP/Gmail) --------
    EMAIL_ENABLED: bool = Field(default=True)  # activa envío de emails
    EMAIL_FROM: str = Field(default="khrisriosblum@gmail.com")
    EMAIL_TO: str = Field(default="khrisriosblum@gmail.com")
    SMTP_HOST: str = Field(default="smtp.gmail.com")
    SMTP_PORT: int = Field(default=587)         # 587 = TLS, 465 = SSL
    SMTP_USER: str = Field(default="khrisriosblum@gmail.com")
    # *** Has pedido incluir la clave aquí ***
    # Para Gmail es una "App Password" de 16 caracteres (puede llevar espacios).
    SMTP_PASS: str = Field(default="xaey rclm gxan ywyd")
    SMTP_TLS: bool = Field(default=True)        # True = STARTTLS (puerto 587)

    # Correo también en pruebas (DRY_RUN). En producción mejor False.
    EMAIL_ON_DRY_RUN: bool = Field(default=False)
    # True = cuerpo del email = texto exacto del post (hashtags incluidos)
    EMAIL_TEXT_ONLY: bool = Field(default=True)

    # Carga de variables desde .env / Environment (Render las sobreescribe)
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )

settings = Settings()
