#чтобы было легче вытаскивать данные, преобразование данных
#хз зачем, но в видосике было
from django.db.models import fields
from rest_framework import serializers
from mylibrary.models import Authors, Genres, Books, Publishers

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields=('id','Name', 'BirthDate')

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genres
        fields=( 'id','Name')

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=( 'id','Title', 'Author_id', 'Genre_id', 'PublishDate', 'Publisher_id')

class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publishers
        fields=( 'id','Name', 'Address')