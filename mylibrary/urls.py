from django.conf.urls import url
from mylibrary import views


urlpatterns=[

    url(r'^book$', views.BooksAPI),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BooksAPIID),
    url(r'^book/genre/(?P<NameGenre>[a-z]+)/$', views.BooksByGenreAPI),
    url(r'^book/tag/(?P<TagName>[a-z]+)/$', views.BooksByTagAPI),
    url(r'^book/all/(?P<Name>[a-z]+)/$', views.BooksByAllFieldsAPI),
    url(r'^book/author/(?P<NameAuthor>[a-z]+)/$', views.BooksByAuthorAPI),
    url(r'^book/publisher/count/(?P<NamePublisher>[a-z]+)/$', views.CountBooksbyPublisherAPI),
    url(r'^author$', views.AuthorsAPI),
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorsAPIID),
    url(r'^genre$', views.GenresAPI),
    url(r'^genre/(?P<pk>[0-9]+)/$', views.GenresAPIID),
    url(r'^publisher$', views.PublishersAPI),
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublishersAPIID),
]