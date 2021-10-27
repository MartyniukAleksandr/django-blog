from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email
