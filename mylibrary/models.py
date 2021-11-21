from django.db import models

# Create your models here.

class Authors(models.Model):
    Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=500)
    BirthDate = models.DateTimeField('BirthDate')

class Genres(models.Model):
    Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=500)

class Publishers(models.Model):
    Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=500)
    Address = models.CharField('Address', max_length=500)


class Books(models.Model):
    Id = models.IntegerField('Id')
    Title = models.CharField('Title', max_length=500)
    AuthorId = models.ManyToManyField(Authors, verbose_name='AuthorId', related_name='AuthorId')
    GenreId = models.ManyToManyField(Genres, verbose_name='GenreId', related_name='GenreId')
    PublishDate = models.DateTimeField('PublishDate')
    PublisherId = models.ManyToManyField(Publishers, verbose_name='PublisherId', related_name='PublisherId')
