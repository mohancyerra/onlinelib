from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN number</a>')
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	#genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

class Genre(models.Model):
	name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

	def __str__(self):
		return self.name

class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Book availability',
	)

	class Meta:
		ordering = ['due_back']

	def __str__(self):
		#return f'{self.id} ({self.book.title})'
		return self.book

class Author(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	date_of_birth = models.DateField(null= True, blank = True)
	date_of_death = models.DateField('Died', null= True, blank = True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		"""Returns the url to access a particular author instance."""
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		#return f'{self.last_name}, {self.first_name}'
		return self.last_name