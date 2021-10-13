from django.contrib import admin
from .models import Category, Article, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}


class ReviewInline(admin.TabularInline):
    """Все отзывы прикрепленные к данной статье"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')  # поля только для чтения


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at', 'image', 'category', 'draft')
    list_filter = ('draft', 'updated_at', 'created_at', 'author',)
    search_fields = ('title', 'content', 'category__name')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['draft', 'created_at']
    inlines = [ReviewInline]
    save_on_top = True  # переносим(дублируем) меню вверх для удобства
    list_editable = ('draft',)  # свойство которое помогает нам редактировать поле "Черновик"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'parent', 'article', 'id')
    readonly_fields = ('name', 'email')  # поля только для чтения


admin.site.site_title = "Мой блог" # меняем title админ панели
admin.site.site_header = "Мой блог"
