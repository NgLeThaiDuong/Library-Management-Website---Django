# Generated by Django 3.1.2 on 2021-01-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmagapp', '0022_auto_20210107_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_cover', verbose_name='Bìa sách'),
        ),
    ]
