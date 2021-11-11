from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from .forms import ContactForm, EmailContactForm
from .tasks import send_greeting_email, get_email


class ContactView(View):
    """подписка на рассылку"""

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Благодарим Вас за подписку!')
            send_greeting_email.delay(form.instance.email)  # отправка email
            return redirect('/')
        else:
            messages.error(request, 'Упс! Что то пошло не так! Повторите попытку!')


class EmailContactView(View):
    """Отправка письма """

    def get(self, request):
        form = EmailContactForm()
        return render(request, 'contact/contact.html', {'form': form, 'title': 'Контакты'})

    def post(self, request):
        form = EmailContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['subject']}. От {cd['name']}. Email: {cd['email']}"
            from_email = cd['email']
            to_email = 'fobos339@gmail.com'
            message = cd['message']
            get_email.delay(
                subject,
                message,
                from_email,
                to_email
            )
            messages.success(request, 'Спасибо! Ваше сообщение отправлено!')
            return redirect('/')
        else:
            messages.error(request, 'Упс! Что то пошло не так! Повторите попытку!')
