DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "testdb",
    }
}

INSTALLED_APPS = ( "pandasjsonfield",)

import random
key_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = ''.join([
    random.SystemRandom().choice(key_chars) for i in range(50)
])
