from django.urls import path
from . import views
from .views import add_book_review
from .views import add_book
urlpatterns = [
    path('', views.home_page, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/review/', add_book_review, name='add_book_review'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/add/', add_book, name='add_book'),
]