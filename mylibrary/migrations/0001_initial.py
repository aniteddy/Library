# Generated by Django 3.2.9 on 2021-11-21 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500, verbose_name='Name')),
                ('BirthDate', models.DateTimeField(verbose_name='BirthDate')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, verbose_name='Title')),
                ('AuthorId', models.CharField(max_length=255, verbose_name='AuthorId')),
                ('GenreId', models.CharField(max_length=255, verbose_name='GenreId')),
                ('PublishDate', models.DateTimeField(verbose_name='PublishDate')),
                ('PublisherId', models.CharField(max_length=255, verbose_name='PublisherId')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500, verbose_name='Name')),
                ('Address', models.CharField(max_length=500, verbose_name='Address')),
            ],
        ),
    ]
