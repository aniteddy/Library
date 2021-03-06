# Generated by Django 3.2.9 on 2021-11-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, verbose_name='TagName')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='Tag',
            field=models.ManyToManyField(to='mylibrary.Tag'),
        ),
    ]
