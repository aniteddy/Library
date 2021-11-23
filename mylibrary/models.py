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
    #AuthorId = models.CharField('AuthorId', max_length=255)
    AuthorId = models.ForeignKey('Authors', on_delete=models.SET_NULL, null=True)
    #GenreId = models.CharField('GenreId', max_length=255)
    GenreId = models.ForeignKey('Genres', on_delete=models.SET_NULL, null=True)
    PublishDate = models.DateTimeField('PublishDate')
    #PublisherId = models.CharField('PublisherId', max_length=255)
    PublisherId = models.ForeignKey('Publishers', on_delete=models.SET_NULL, null=True)