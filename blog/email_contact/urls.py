from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('delete/<int:pk>/', views.DeleteContactView.as_view(), name='contact_delete'),
    path('send/', views.EmailContactView.as_view(), name='email_contact'),
]
