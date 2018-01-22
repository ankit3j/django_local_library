from django.conf.urls import url
from . import views
from django.urls import path

#app_name = 'catalog'
urlpatterns = [
	url(r'^$', views.index, name='index'), 
	url(r'^books/$', views.BookListView.as_view(), name='books'),
	url(r'book/(?P<pk>[0-9]*)/$', views.BookDetailView.as_view(), name='book-detail'),
	url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
	url(r'author/(?P<pk>[0-9]*)/$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
	url(r'^borrowed/$', views.AllLoanedBooksListView.as_view(), name='all-borrowed'),
	path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
	url(r'^author/create/', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>[0-9]+)/update/', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>[0-9]+)/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    url(r'^book/create/', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>[0-9]+)/update/', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>[0-9]+)/delete/', views.BookDelete.as_view(), name='book_delete'),

]