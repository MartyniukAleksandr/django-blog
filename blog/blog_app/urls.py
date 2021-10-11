from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('blog_datail', blog_detail, name='blog_detail')
]
