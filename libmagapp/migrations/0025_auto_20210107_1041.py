# Generated by Django 3.1.2 on 2021-01-07 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmagapp', '0024_auto_20210107_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, default='book_cover\\default_book_cover.jpg', null=True, upload_to='book_cover', verbose_name='Bìa sách'),
        ),
    ]
