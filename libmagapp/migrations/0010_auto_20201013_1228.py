# Generated by Django 3.1.2 on 2020-10-13 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmagapp', '0009_auto_20201013_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='email',
            field=models.CharField(max_length=254, verbose_name='Địa chỉ email'),
        ),
    ]
