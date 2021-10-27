from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from .forms import ContactForm


class ContactView(View):
    """подписка на рассылку"""

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Благодарим Вас за подписку!')
            return redirect('/')
        else:
            messages.error(request, 'Упс! Что то пошло не так! Повторите попытку!')
