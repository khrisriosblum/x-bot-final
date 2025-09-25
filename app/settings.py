
from pydantic import BaseSettings, Field
from typing import List
import os

class Settings(BaseSettings):
    # Excel
    EXCEL_PATH: str = Field(default=os.getenv("EXCEL_PATH", "data/tracks.xlsx"))
    # Timezone
    TIMEZONE: str = Field(default=os.getenv("TIMEZONE", "Europe/Madrid"))
    # Posting times (24h, HH:MM)
    POST_TIMES: str = Field(default=os.getenv("POST_TIMES", "10:00,13:00,16:00,19:00,22:00"))
    # Random jitter window in minutes (+/-)
    JITTER_MINUTES: int = Field(default=int(os.getenv("JITTER_MINUTES", "15")))
    # Sleep before publish (to allow URL preview as requested)
    SLEEP_BEFORE_PUBLISH: int = Field(default=int(os.getenv("SLEEP_BEFORE_PUBLISH", "15")))
    # Dedup window (days)
    DEDUP_DAYS: int = Field(default=int(os.getenv("DEDUP_DAYS", "70")))
    # "Recent" window (days)
    RECENT_DAYS: int = Field(default=int(os.getenv("RECENT_DAYS", "2")))
    # Special 19:00 rules
    SOUND_CLOUD_EVERY_N_DAYS: int = Field(default=int(os.getenv("SOUND_CLOUD_EVERY_N_DAYS", "3")))
    SPOTIFY_TOPS_EVERY_N_DAYS: int = Field(default=int(os.getenv("SPOTIFY_TOPS_EVERY_N_DAYS", "10")))
    # Start date for modulo math (YYYY-MM-DD)
    START_DATE: str = Field(default=os.getenv("START_DATE", "2025-01-01"))
    # Tweepy / X credentials
    X_API_KEY: str = Field(default=os.getenv("X_API_KEY", ""))
    X_API_SECRET: str = Field(default=os.getenv("X_API_SECRET", ""))
    X_ACCESS_TOKEN: str = Field(default=os.getenv("X_ACCESS_TOKEN", ""))
    X_ACCESS_SECRET: str = Field(default=os.getenv("X_ACCESS_SECRET", ""))
    # Dry run (don't actually post to X)
    DRY_RUN: bool = Field(default=os.getenv("DRY_RUN", "true").lower() in ("1","true","yes"))
    # SQLite path (attach persistent disk in Render and point to /data/bot.db)
    DB_PATH: str = Field(default=os.getenv("DB_PATH", "/data/bot.db"))
    # Web server port
    PORT: int = Field(default=int(os.getenv("PORT", "8000")))

        # Facebook Page credentials
        # The ID of the Facebook Page where posts should be published. Obtain this
        # from the page’s About section or via the Graph API. Set via env var
        # FB_PAGE_ID. If empty, Facebook publishing will be skipped.
        FB_PAGE_ID: str = Field(default=os.getenv("FB_PAGE_ID", ""))
        # Long‑lived Page access token with `pages_manage_posts` permission.
        # Generate this in the Meta Developer portal and set via env var
        # FB_PAGE_ACCESS_TOKEN. If empty, Facebook publishing will be skipped.
        FB_PAGE_ACCESS_TOKEN: str = Field(default=os.getenv("FB_PAGE_ACCESS_TOKEN", ""))

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
