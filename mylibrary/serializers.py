#чтобы было легче вытаскивать данные, преобразование данных
#хз зачем, но в видосике было
from django.db.models import fields
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from mylibrary.models import Authors, Genres, Books, Publishers, Tags

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

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'Name')


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publishers
        fields=( 'id','Name', 'Address')

class AllBooksInformationSerializer(serializers.ModelSerializer):
    Genre = GenresSerializer(many=False)
    Author = AuthorsSerializer(many=False)
    Publisher = PublishersSerializer(many=False)
    class Meta:
        model=Books
        fields='__all__'


