# Generated by Django 3.2.8 on 2021-10-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_article_short_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_content',
            field=models.TextField(default='Нет описания', max_length=300, verbose_name='Краткое описание'),
        ),
    ]
