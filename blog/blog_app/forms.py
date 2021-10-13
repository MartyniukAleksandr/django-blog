from django import forms

from .models import Reviews

class ReviewForm(forms.ModelForm):
    """Форма отзывов(комментариев)"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')