from django.core.mail import send_mail


def send_greeting(email):
    """Отправка письма приветствия"""
    send_mail(
        'Мы Вас тоже любим!',
        'Благодарим за подписку на наш блог',
        'fobos339@gmail.com',
        [email],
        fail_silently=False,
    )
