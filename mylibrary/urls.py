from django.conf.urls import url
from mylibrary import views


urlpatterns=[

    url(r'^book$', views.BooksAPI),
    #url(r'book/<int:pk>/', views.BooksAPIID),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BooksAPIID),
    #url(r'^author$', views.AuthorsAPI),
    url(r'^author/([0-9]+)$', views.AuthorsAPI),
    #url(r'^genre$', views.GenresAPI),
    url(r'^genre/([0-9]+)$', views.GenresAPI),
    #url(r'^publisher$', views.PublishersAPI),
    url(r'^publisher/([0-9]+)$', views.PublishersAPI),
]