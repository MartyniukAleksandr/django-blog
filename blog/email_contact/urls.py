from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('send/', views.EmailContactView.as_view(), name='email_contact')
]
