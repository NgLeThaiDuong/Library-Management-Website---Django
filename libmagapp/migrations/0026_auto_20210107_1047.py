# Generated by Django 3.1.2 on 2021-01-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmagapp', '0025_auto_20210107_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, default='media/book_cover/default_book_cover.jpg', null=True, upload_to='media/book_cover', verbose_name='Bìa sách'),
        ),
    ]
