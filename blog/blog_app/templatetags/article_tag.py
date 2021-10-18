from django import template

from blog_app.models import Category
from taggit.models import Tag  # импорт из taggit.models модель Tag

register = template.Library()


@register.simple_tag()
def get_categories():
    """Возвращает список категорий"""
    return Category.objects.all()


@register.simple_tag()
def get_tags():
    """Возвращает список тегов"""
    return Tag.objects.all()
