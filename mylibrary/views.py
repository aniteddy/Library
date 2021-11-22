from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from mylibrary.models import Authors, Genres, Books, Publishers
from mylibrary.serializers import AuthorsSerializer, GenresSerializer,BooksSerializer,PublishersSerializer

# Create your views here

@csrf_exempt
def BooksApi(request, id=0):
    if request.method=='GET':
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
        books = Books.objects.get(Title = books_data['Title'])
        books_serializer=BooksSerializer(books,data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method=='DELETE':
        books = Books.objects.get(Id=id)
        books.delete()
        return JsonResponse('Delete Successfully', safe=False)