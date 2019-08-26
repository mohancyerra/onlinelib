from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name = 'books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('sign_up', views.Sign_up.as_view(), name='sign_up')
]