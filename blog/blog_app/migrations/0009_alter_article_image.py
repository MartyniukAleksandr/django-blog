# Generated by Django 3.2.8 on 2021-11-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='blog_images/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
