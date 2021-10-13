from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'
    """переводим имя преложения в админке 
    в __init__.py, нужно прописать 
    default_app_config = 'blog_app.apps.BlogAppConfig'"""
    verbose_name = 'Блог'
