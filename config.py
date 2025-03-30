import os

class Config(object):
    API_ID    = os.environ.get("API_ID", "23069582")
API_HASH  = os.environ.get("API_HASH", "b3b56eaf67828684f54d540f684fdf1f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7360145974:AAF2uRappsLXFrKP8SVszjkliIp8nGj8Sl8")
    AUTH_USER = os.environ.get('AUTH_USERS', '1780523256').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " ♛𝕸𝖊𝖊𝖓𝖆 𝖏𝖎♛™ "
