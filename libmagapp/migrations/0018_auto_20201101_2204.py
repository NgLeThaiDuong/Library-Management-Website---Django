# Generated by Django 3.1.2 on 2020-11-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmagapp', '0017_auto_20201101_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.IntegerField(choices=[(0, 'Generalities'), (1, 'Philosophy & psychology'), (2, 'Religion'), (3, 'Social sciences'), (4, 'Languages'), (5, 'Natural sciences & mathematics'), (6, 'Technology'), (7, 'The arts'), (8, 'Literature & rhetoric'), (9, ' Geography & history')], default=None, verbose_name='Chu de'),
        ),
    ]
