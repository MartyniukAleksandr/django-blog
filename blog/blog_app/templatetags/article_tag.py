from django import template
from blog_app.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    """Возвращает список категорий"""
    return Category.objects.all()