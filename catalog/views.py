from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
def index(request):
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

  # Available books (status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()
	
	context = {
	'num_books': num_books,
	'num_instances': num_instances,
	'num_instances_available': num_instances_available,
	'num_authors': num_authors,
  }
	return render(request, 'index.html', context = context)

class BookListView(generic.TemplateView):
	model = Book
	def get_context_data(self, **kwargs):
		# call base implimentation first to get the context
		context = super(BookListView, self).get_context_data(**kwargs)
		# create any data and add it to the context
		context['some_data'] = 'This is just some data'
		return render

class AuthorListView(generic.ListView):
	model = Author
class BookDetailView(generic.DetailView):
	model = Book

	def book_detail_view(request, primary_key):
		try:
			book =Book.objects.get(pk = primary_key)
		except Book.DoesNotExist:
			raise Http404('Book does not exist')
		return render(request, 'catalog/book_detail.html', context={'book': book})

class Sign_up():
	model = Sign_up
	def __str__(self):
		return model.name


