import time
from .settings import settings

def post_to_x(text: str) -> dict:
    """
    Publica un tweet. Si DRY_RUN=True, simplemente lo registra en los logs.
    """
    if settings.DRY_RUN:
        print("[DRY_RUN] Would post:\n", text)
        time.sleep(1)
        return {"status": "dry_run"}

    # Espera antes de publicar (para permitir previsualizar la URL, si procede)
    wait_s = max(0, settings.SLEEP_BEFORE_PUBLISH)
    if wait_s:
        time.sleep(wait_s)

    try:
        import tweepy
        # Crear un cliente de la API v2 con autenticación de usuario
        client = tweepy.Client(
            consumer_key=settings.X_API_KEY,
            consumer_secret=settings.X_API_SECRET,
            access_token=settings.X_ACCESS_TOKEN,
            access_token_secret=settings.X_ACCESS_SECRET,
        )
        response = client.create_tweet(text=text)
        tweet_id = str(response.data.get('id')) if response and response.data else None
        return {"status": "ok", "id": tweet_id}
    except Exception as e:
        return {"status": "error", "error": str(e)}
