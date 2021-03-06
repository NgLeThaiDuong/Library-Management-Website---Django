# Generated by Django 3.1.2 on 2021-01-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmagapp', '0019_merge_20210107_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pub_year',
            new_name='pubdate',
        ),
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(null=True, upload_to='book_cover', verbose_name='Bìa sách'),
        ),
        migrations.AddField(
            model_name='member',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar', verbose_name='Ảnh đại diện'),
        ),
    ]
