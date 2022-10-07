from django.apps import AppConfig

# files configuration field user_account (it's auto)

class UserAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_account'
