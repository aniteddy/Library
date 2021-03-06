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

class Tags(models.Model):
    Name = models.CharField('TagName', max_length=250)

class Books(models.Model):
    #Id = models.IntegerField('Id')
    Title = models.CharField('Title', max_length=250)
    Author= models.ForeignKey('Authors',models.DO_NOTHING, max_length=250)
    Genre = models.ForeignKey('Genres',models.DO_NOTHING, max_length=250)
    PublishDate = models.DateTimeField('PublishDate')
    Publisher = models.ForeignKey('Publishers',models.DO_NOTHING, max_length=250)
    Tag = models.ManyToManyField(Tags)



#Заполнение таблицы в БД
def AddDatatoDB():
    #Authors
    Mary = Authors.objects.create(Name = 'Mary', BirthDate = '1979-11-29 00:00:30')
    Barry = Authors.objects.create( Name = 'Barry', BirthDate = '1980-11-29 00:00:30')
    Ichigo = Authors.objects.create(Name = 'Ichigo', BirthDate = '1955-11-29 00:00:30')
    #Genres
    Story = Genres.objects.create(Name='Story')
    Fantasy = Genres.objects.create(Name='Fantasy')
    FairyTail = Genres.objects.create(Name='FairyTail')
    # Publishers
    Kokoriki = Publishers.objects.create(Name = 'Kokoriki', Address = 'Shararam')
    Park = Publishers.objects.create(Name = 'Park', Address = 'Seven street')
    LasNoches = Publishers.objects.create(Name = 'LasNoches', Address = 'Empty')
    #Tags
    Anime = Tags.objects.create(Name = 'Anime')
    Stone = Tags.objects.create(Name = 'Stone')
    Eat = Tags.objects.create(Name = 'Eat')
    Fight = Tags.objects.create(Name = 'Fight')
    Soul = Tags.objects.create(Name = 'Soul')
    #Books
    Bbm = Books.objects.create(Title = 'Bee bite me', PublishDate ='2000-11-29 00:00:30', Author_id = Barry.id, Genre_id = Fantasy.id, Publisher_id = Kokoriki.id)
    Raspberry = Books.objects.create(Title = 'Raspberry', PublishDate ='2010-11-29 00:00:30', Author_id = Barry.id, Genre_id = FairyTail.id, Publisher_id = Kokoriki.id)
    Amber = Books.objects.create(Title = 'Amber', PublishDate ='2000-11-29 00:00:30', Author_id = Mary.id, Genre_id = Story.id, Publisher_id = Park.id)
    Bleach = Books.objects.create(Title = 'Bleach', PublishDate ='2010-11-30 00:00:30', Author_id = Ichigo.id, Genre_id = Fantasy.id, Publisher_id = LasNoches.id)

    Bbm.Tag.add(Fight)
    Raspberry.Tag.add(Eat)
    Bleach.Tag.add(Anime, Fight, Soul)



#AddDatatoDB()