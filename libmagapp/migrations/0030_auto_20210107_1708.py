# Generated by Django 3.1.2 on 2021-01-07 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libmagapp', '0029_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklending',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libmagapp.book', verbose_name='Mã sách được mượn'),
        ),
        migrations.AlterField(
            model_name='booklending',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libmagapp.member', verbose_name='Mã thành viên mượn'),
        ),
    ]