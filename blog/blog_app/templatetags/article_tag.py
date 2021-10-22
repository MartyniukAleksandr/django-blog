from django import template

from blog_app.models import Category, Article
from taggit.models import Tag  # импорт из taggit.models модель Tag
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def get_categories():
    """Возвращает список категорий"""
    return Category.objects.all()


@register.simple_tag()
def get_tags():
    """Возвращает список тегов"""
    return Tag.objects.all()


@register.simple_tag()
def get_archives():
    """Возвращает список архивов"""
    return Article.objects.dates('created_at', 'month', order='DESC')


@register.inclusion_tag('tags/popular_articles.html')
def get_popular_articles(count=None):
    """Возвращает список популярных статей"""
    popular_articles = Article.objects.annotate(
        num_comments=Count('reviews')
    ).order_by('-num_comments').filter(draft=False)[:count]
    return {
        'popular_articles': popular_articles
    }
