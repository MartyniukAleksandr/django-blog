from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории блога"""
    name = models.CharField(max_length=150, blank=False, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=150, unique=True, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Построение абсолютного пути категории"""
        return reverse('article_category_list', kwargs={'slug': self.slug})


class Article(models.Model):
    """Статьи блога"""
    title = models.CharField(max_length=256, blank=False, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField(max_length=256, db_index=True)
    short_content = models.TextField(verbose_name='Краткое описание', max_length=300, default='Нет описания')
    content = models.TextField(blank=True, default='Нет описания', verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d', verbose_name='Изображение', blank=True)
    draft = models.BooleanField(verbose_name='Черновик', default=False)
    author = models.CharField(verbose_name='Автор', blank=False, max_length=150)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Построение абсолютного пути"""
        return reverse('article_detail', kwargs={'slug': self.slug})


class Reviews(models.Model):
    """Отзывы(коментарии)"""
    email = models.EmailField()
    name = models.CharField(verbose_name='Имя', max_length=110)
    text = models.TextField(verbose_name='Сообщение', max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации отзыва', )
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    article = models.ForeignKey(Article, verbose_name='статья', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.article}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
