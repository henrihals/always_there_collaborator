from django.apps import AppConfig

# files configuration field Blog_user (it's auto)

class BlogUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_user'
