from django.db import models
from django.urls import reverse
from blog.settings import BASE_URL


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

    def get_absolute_url(self):
        """Построение абсолютного пути"""
        return reverse('contact_delete', kwargs={'pk': self.pk})

    def get_truly_absolute_url(self):
        """Возвращают полный абсолютный путь к примеру http://localhost:8000/akessesuary-dlya-vyazanyh-veshej/"""
        return BASE_URL + self.get_absolute_url()
