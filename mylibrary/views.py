from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from mylibrary.models import Authors, Genres, Books, Publishers
from mylibrary.serializers import AuthorsSerializer, GenresSerializer,BooksSerializer,PublishersSerializer

# Create your views here
@csrf_exempt
def BooksByGenreAPI(request, NameGenre):
    if request.method=='GET':
        #genre = Genres.objects.filter(Name=NameGenre).values_list('id', flat =True)[0]
        #genre = Genres.objects.filter(Name=NameGenre).select_related('Books')
        #book = Books.objects.filter(Genre_id=genre).all()
        book=Books.objects.filter(Genre__Name=NameGenre)
        #book= Books.objects.filter(GenreId=genre)
        #book= Books.objects.select_related()
        books_serializer = BooksSerializer(book,many=True)
        return JsonResponse(books_serializer.data, safe=False)

@csrf_exempt
def BooksAPIID(request, pk):
    if request.method=='GET':
        book = Books.objects.get(id=pk)
        books_serializer = BooksSerializer(book,many=False)
        return JsonResponse(books_serializer.data)
@csrf_exempt
def AuthorsAPIID(request, pk):
    if request.method=='GET':
        author = Authors.objects.get(id=pk)
        authors_serializer = AuthorsSerializer(author,many=False)
        return JsonResponse(authors_serializer.data)
@csrf_exempt
def GenresAPIID(request, pk):
    if request.method=='GET':
        genre = Genres.objects.get(id=pk)
        genres_serializer = GenresSerializer(genre,many=False)
        return JsonResponse(genres_serializer.data)
@csrf_exempt
def PublishersAPIID(request, pk):
    if request.method=='GET':
        publisher = Publishers.objects.get(id=pk)
        publishers_serializer = PublishersSerializer(publisher,many=False)
        return JsonResponse(publishers_serializer.data)

@csrf_exempt
def BooksAPI(request):
    if request.method=='LIST':
        books = Books.objects.all()
        books_serializer = BooksSerializer(books,many=True)
        return JsonResponse(books_serializer.data, safe=False)
    elif request.method=='POST':
        books_data=JSONParser().parse(request)
        books_serializer= BooksSerializer(data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='PUT':
        books_data=JSONParser().parse(request)
        books = Books.objects.get(id = books_data['id'])
        books_serializer=BooksSerializer(books,data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method=='DELETE':
        books_data=JSONParser().parse(request)
        books = Books.objects.get(id = books_data['id'])
        books.delete()
        return JsonResponse('Delete Successfully', safe=False)

@csrf_exempt
def AuthorsAPI(request, id=0):
    if request.method=='LIST':
        authors = Authors.objects.all()
        authors_serializer =AuthorsSerializer(authors,many=True)
        return JsonResponse(authors_serializer.data, safe=False)
    elif request.method=='POST':
        authors_data=JSONParser().parse(request)
        authors_serializer= AuthorsSerializer(data=authors_data)
        if authors_serializer.is_valid():
            authors_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='PUT':
        authors_data=JSONParser().parse(request)
        authors = Authors.objects.get(id = authors_data['id'])
        authors_serializer=AuthorsSerializer(authors,data=authors_data)
        if authors_serializer.is_valid():
            authors_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method=='DELETE':
        authors_data=JSONParser().parse(request)
        authors = Authors.objects.get(id = authors_data['id'])
        authors.delete()
        return JsonResponse('Delete Successfully', safe=False)


@csrf_exempt
def GenresAPI(request, id=0):
    if request.method=='LIST':
        genres = Genres.objects.all()
        genres_serializer =GenresSerializer(genres,many=True)
        return JsonResponse(genres_serializer.data, safe=False)
    elif request.method=='POST':
        genres_data=JSONParser().parse(request)
        genres_serializer= GenresSerializer(data=genres_data)
        if genres_serializer.is_valid():
            genres_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='PUT':
        genres_data=JSONParser().parse(request)
        genres = Genres.objects.get(id = genres_data['id'])
        genres_serializer=GenresSerializer(genres,data=genres_data)
        if genres_serializer.is_valid():
            genres_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method=='DELETE':
        genres_data=JSONParser().parse(request)
        genres = Genres.objects.get(id = genres_data['id'])
        genres.delete()
        return JsonResponse('Delete Successfully', safe=False)


@csrf_exempt
def PublishersAPI(request):
    if request.method=='LIST':
        publishers = Publishers.objects.all()
        publishers_serializer =PublishersSerializer(publishers,many=True)
        return JsonResponse(publishers_serializer.data, safe=False)
    elif request.method=='POST':
        publishers_data=JSONParser().parse(request)
        publishers_serializer= PublishersSerializer(data=publishers_data)
        if publishers_serializer.is_valid():
            publishers_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='PUT':
        publishers_data=JSONParser().parse(request)
        publishers = Publishers.objects.get(id = publishers_data['id'])
        publishers_serializer=PublishersSerializer(publishers,data=publishers_data)
        if publishers_serializer.is_valid():
            publishers_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method=='DELETE':
        publishers_data=JSONParser().parse(request)
        publishers = Publishers.objects.get(id = publishers_data['id'])
        publishers.delete()
        return JsonResponse('Delete Successfully', safe=False)