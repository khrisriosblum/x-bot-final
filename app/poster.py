
import time
from .settings import settings
import requests

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
            # Use Tweepy v2 client to create a tweet. Recent changes in X's API
            # restrict access to the v1.1 `statuses/update` endpoint unless
            # applications have elevated access. Tweepy’s `Client` uses the v2
            # endpoint (`POST /2/tweets`) when authenticated with user context.
            # This requires the same consumer key/secret and access token/secret
            # values but will work on basic/elevated tiers as long as the
            # `tweet.write` scope is enabled for the app.  If a bearer token is
            # available it can also be passed in, but is not strictly required
            # for user‑context posting.
            client = tweepy.Client(
                consumer_key=settings.X_API_KEY,
                consumer_secret=settings.X_API_SECRET,
                access_token=settings.X_ACCESS_TOKEN,
                access_token_secret=settings.X_ACCESS_SECRET,
                # Do not set wait_on_rate_limit here because create_tweet is
                # unlikely to hit rate limits during normal operation.
            )
            response = client.create_tweet(text=text)
            # `response.data` is a dict like {'id': '<tweet_id>', 'text': '<text>'}
            tweet_id = str(response.data.get('id')) if response and response.data else None
            return {"status": "ok", "id": tweet_id}
        except Exception as e:
            # Return the exception message to help with debugging in Render logs
            return {"status": "error", "error": str(e)}

# New function to post to a Facebook Page using the Graph API.
# If FB_PAGE_ID or FB_PAGE_ACCESS_TOKEN are not set, or DRY_RUN is True,
# the function logs the intended post and returns `dry_run`.
def post_to_facebook(text: str, link: str | None = None) -> dict:
    """
    Publish a post to a Facebook Page feed. Accepts a message and an
    optional link. Returns a dict similar to post_to_x with keys
    "status", and optionally "id" or "error".
    """
    # If DRY_RUN is enabled or credentials are missing, skip real posting
    if settings.DRY_RUN or not settings.FB_PAGE_ID or not settings.FB_PAGE_ACCESS_TOKEN:
        print("[DRY_RUN FB] Would post:\n", text)
        return {"status": "dry_run"}

    # Respect the same wait period as the X posting
    wait_s = max(0, settings.SLEEP_BEFORE_PUBLISH)
    if wait_s:
        time.sleep(wait_s)

    try:
        params = {
            "message": text,
            "access_token": settings.FB_PAGE_ACCESS_TOKEN,
        }
        if link:
            params["link"] = link
        resp = requests.post(
            f"https://graph.facebook.com/v19.0/{settings.FB_PAGE_ID}/feed", params=params
        )
        if 200 <= resp.status_code < 300:
            data = resp.json() if resp.content else {}
            post_id = data.get("id")
            return {"status": "ok", "id": post_id}
        else:
            return {"status": "error", "error": resp.text}
    except Exception as e:
        return {"status": "error", "error": str(e)}
