from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Article
from .forms import ReviewForm


class IndexView(ListView):
    """Список статей"""
    model = Article
    queryset = Article.objects.filter(draft=False)
    context_object_name = 'articles'
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    """Полное описание статьи"""
    model = Article
    slug_field = 'slug'
    template_name = 'blog_detail.html'


class AddReview(View):
    """Отзывы(комментарии)"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)  # приостанавливаем запись формы
            if request.POST.get("parent", None):  # привязка родительского коментария
                form.parent_id = int(request.POST.get("parent"))
            form.article = article  # вносим новыу изменения...
            form.save()  # и сохраняем их в нашу БД
        return redirect(article.get_absolute_url())


class CategoryView(ListView):
    """Категории статей"""
    model = Article
    # queryset = Article.objects.filter(draft=False)
    context_object_name = 'articles'
    template_name = 'index.html'

    def get_queryset(self):
        """Фильтруем статьи по категориям"""
        return Article.objects.filter(category__slug=self.kwargs['slug'], draft=False)


class TagView(ListView):
    """Теги сайта"""
    model = Article
    # queryset = Article.objects.filter(draft=False)
    context_object_name = 'articles'
    template_name = 'index.html'

    def get_queryset(self):
        """Фильтруем статьи по ключевым словам(тегам)"""
        return Article.objects.filter(tags__slug=self.kwargs['slug'], draft=False)
