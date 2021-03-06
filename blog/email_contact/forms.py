from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""

    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите Ваш email'
                }
            )
        }
        labels = {
            'email': ''
        }


class EmailContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }
        ),
        label=''
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите почтовый адрес',
            }
        ),
        label=''

    )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите тему сообщения',
            }
        ),
        label=''
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'cols': '200',
                'rows': '15',
                'placeholder': 'Введите сообщения',
            }
        ),
        label=''
    )
