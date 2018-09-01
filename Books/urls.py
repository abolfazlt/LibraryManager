from django.conf.urls import url , include

from Books.models import Book , RequestedBooks
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Books'

urlpatterns = [
    # /books/
    url(r'^$', views.index, name='index'),

    # /books/register/
    url(r'^register/$', views.register, name='register'),

    # /books/<book_id>/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),

    # /books/logout_user/
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /books/login_user/
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /books/add
    url(r'^add/$', views.add_book, name='add_book'),

    #/books/request_a_book
     url(r'^request_a_book/$', views.request_a_book, name='request_a_book'),

    #/books/requestedBooks
    url(r'^requested_Books/$', views.requested_Books, name='requested_Books'),

    # /books/update/2/
    url(r'^update/(?P<book_id>[0-9]+)/$', views.update_book, name='book-update'),

    # /books/delete/2
    url(r'^delete/(?P<pk>[0-9]+)/$', views.BookDelete.as_view(), name='book-delete'),

    # /books/2/return/
    url(r'^(?P<book_id>[0-9]+)/return/$', views.return_book, name='book-return'),

    # /books/2/borrow/
    url(r'^(?P<book_id>[0-9]+)/borrow/$', views.borrow_book, name='book-borrow'),

    # /books/search/ (text goes here) /
     url(r'^search/$', views.search, name='search'),
    #
    # url('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),







]
