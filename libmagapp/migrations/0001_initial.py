# Generated by Django 3.1.2 on 2020-10-11 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('pub_date', models.IntegerField()),
                ('size', models.CharField(max_length=7)),
                ('number_of_pages', models.IntegerField()),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('locatin_identifier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('tel_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('tel_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('resgister_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_date', models.DateField(auto_now_add=True)),
                ('deactive_date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmagapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_date', models.DateField(auto_now_add=True)),
                ('requested_book_title', models.CharField(max_length=255)),
                ('requested_book_author', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmagapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='BookLending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('return_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmagapp.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmagapp.member')),
            ],
        ),
    ]
