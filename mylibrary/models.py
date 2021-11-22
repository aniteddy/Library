from django.db import models

# Create your models here.

class Authors(models.Model):
    #Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=500)
    BirthDate = models.DateTimeField('BirthDate')

class Genres(models.Model):
    #Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=500)

class Publishers(models.Model):
    #Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=500)
    Address = models.CharField('Address', max_length=500)


class Books(models.Model):
    #Id = models.IntegerField('Id')
    Title = models.CharField('Title', max_length=255)
    AuthorId = models.CharField('AuthorId', max_length=255)
    GenreId = models.CharField('GenreId', max_length=255)
    PublishDate = models.DateTimeField('PublishDate')
    PublisherId = models.CharField('PublisherId', max_length=255)