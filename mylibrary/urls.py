from django.conf.urls import url
from mylibrary import views


urlpatterns=[
    url(r'^book$', views.BooksApi),
    url(r'^book/([0-9]+)$', views.BooksApi)
]