import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7672004632:AAHohyBfssnv2Nlscz0tqiji3r1I7pfsdUc")
    API_ID = int(os.environ["API_ID", 23069582]
    API_HASH = os.environ["API_HASH", "b3b56eaf67828684f54d540f684fdf1f"]
    AUTH_USER = os.environ.get('AUTH_USERS', '1780523256').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " ♛𝕸𝖊𝖊𝖓𝖆 𝖏𝖎♛™ "
