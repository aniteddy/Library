from django.conf.urls import url
from mylibrary import views


urlpatterns=[

    url(r'^book$', views.BooksAPI),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BooksAPIID),
    url(r'^author$', views.AuthorsAPI),
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorsAPIID),
    url(r'^genre$', views.GenresAPI),
    url(r'^genre/(?P<pk>[0-9]+)/$', views.GenresAPIID),
    url(r'^publisher$', views.PublishersAPI),
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublishersAPIID),
]