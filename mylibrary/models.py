from django.db import models

# Create your models here.

class Authors(models.Model):
    #Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=250)
    BirthDate = models.DateTimeField('BirthDate')

class Genres(models.Model):
    #Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=250)

class Publishers(models.Model):
    #Id = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=250)
    Address = models.CharField('Address', max_length=250)


class Books(models.Model):
    #Id = models.IntegerField('Id')
    Title = models.CharField('Title', max_length=250)
    Author= models.ForeignKey('Authors',models.DO_NOTHING, max_length=250)
    Genre = models.ForeignKey('Genres',models.DO_NOTHING, max_length=250)
    PublishDate = models.DateTimeField('PublishDate')
    Publisher = models.ForeignKey('Publishers',models.DO_NOTHING, max_length=250)

