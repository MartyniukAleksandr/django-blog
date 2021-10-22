from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.views.generic.dates import MonthArchiveView
from .models import Article
from .forms import ReviewForm


class DataMixin:
    """Класс Mixin для для выноса повторяющихся элементов"""
    model = Article
    paginate_by = 5
    context_object_name = 'articles'
    template_name = 'index.html'


class IndexView(DataMixin, ListView):
    """Список статей"""

    def get_queryset(self):
        """Queryset статей отфильтрованных по полю draft"""
        return Article.objects.filter(draft=False)


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
            form.article = article  # вносим новые изменения...
            form.save()  # и сохраняем их в нашу БД
        return redirect(article.get_absolute_url())


class CategoryView(DataMixin, ListView):
    """Категории статей"""

    def get_queryset(self):
        """Фильтруем статьи по категориям"""
        return Article.objects.filter(category__slug=self.kwargs['slug'], draft=False)


class TagView(DataMixin, ListView):
    """Теги сайта"""

    def get_queryset(self):
        """Фильтруем статьи по ключевым словам(тегам)"""
        return Article.objects.filter(tags__slug=self.kwargs['slug'], draft=False)


class SearchView(DataMixin, ListView):
    """Поиск по названию статей"""

    def get_queryset(self):
        """Фильтрация статей по названию, не учитывая регистер """
        return Article.objects.filter(title__icontains=self.request.GET.get('search_query'))

    def get_context_data(self, *args, **kwargs):
        """Переопределяем context_data чтобы использовать переменную search_query в форме поиска"""
        context = super().get_context_data(*args, **kwargs)
        context['search_query'] = f"&search_query={self.request.GET.get('search_query')}"
        return context


class ArticleMonthArchiveView(DataMixin, MonthArchiveView):
    """Архив блога по месяцам"""
    date_field = "created_at"
    allow_future = True

    def get_queryset(self):
        """Фильтрация записей в архиве по году та месяцу"""
        return Article.objects.filter(
            created_at__year=self.kwargs['year'], created_at__month=self.kwargs['month'], draft=False
        )


# class PopularArticleView(ListView):
#     model = Article
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         return Article.objects.get(id=5)