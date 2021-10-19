from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="article_list_all"),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name="article_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='article_category_list'),
    path('tag/<slug:slug>/', views.TagView.as_view(), name='tags_list'),

]
