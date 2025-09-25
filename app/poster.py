
import time
from .settings import settings

def post_to_x(text: str) -> dict:
    """
    Post a tweet. If DRY_RUN=True, just log/print.
    Returns a dict with {"status": "ok", "id": "..."} or {"status":"dry_run"} or {"status":"error","error":"..."}
    """
    if settings.DRY_RUN:
        print("[DRY_RUN] Would post:\n", text)
        time.sleep(1)
        return {"status": "dry_run"}

    # Wait before publishing (as requested)
    wait_s = max(0, settings.SLEEP_BEFORE_PUBLISH)
    if wait_s:
        time.sleep(wait_s)

    try:
        import tweepy
        auth = tweepy.OAuth1UserHandler(
            settings.X_API_KEY,
            settings.X_API_SECRET,
            settings.X_ACCESS_TOKEN,
            settings.X_ACCESS_SECRET
        )
        api = tweepy.API(auth)
        resp = api.update_status(status=text)
        return {"status": "ok", "id": str(resp.id)}
    except Exception as e:
        return {"status": "error", "error": str(e)}
