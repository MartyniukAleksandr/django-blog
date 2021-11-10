from django.db.models import Count

from blog.celery import app
from .service import send_greeting, send_by_email
from blog_app.models import Article
from .models import Contact

from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives


@app.task
def send_greeting_email(email):
    """Задание celery --> отправка письма с приветствием"""
    send_greeting(email)


@app.task
def send_beat_email():
    """Задание celery --> массовая рассылка писем подписанным пользователям"""
    popular_articles = Article.objects.annotate(
        num_comments=Count('reviews')
    ).order_by('-num_comments').filter(draft=False)[:3]
    contacts = Contact.objects.all()

    email_list = []
    for contact in contacts:
        email_list.append(contact.email)

    msg_html = render_to_string(
        'popular_articles_email/popular_articles.html',
        context={
            'popular_articles': popular_articles,
        }
    )
    msg_subject = 'Возможно вы пропустили'
    msg_from = 'fobos339@gmail.com'

    try:
        msg = EmailMultiAlternatives(msg_subject, msg_html, msg_from, to=email_list)
        msg.content_subtype = 'html'  # Основное содержание - text/html
        msg.mixed_subtype = 'related'  # устанавливает заголовок электронной почты гарантирующий, ...
        # ...что изображения будут отображаться в строке, а не в виде вложений

        for image_view in popular_articles:
            # Создаст встроенное вложение нашей картинки
            image = MIMEImage(image_view.image.read())
            image.add_header('Content-ID', f"<{image_view.image_filename}>")
            msg.attach(image)
        msg.send()
    except Exception as e:
        return f"{e}\nIn the table 'Contact' in the database in the 'e-mail' field NO data"


@app.task
def get_email(subject, message, from_email, to_email):
    """Задание celery --> получение письма от посетителя сайта"""
    send_by_email(subject, message, from_email, to_email)
