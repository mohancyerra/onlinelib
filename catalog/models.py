from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.
'''
class MyModelName(models.Model):
	my_field_name = models.CharField(max_length = 20, help_text = 'Enter field doccumentation')

	class Meta:
		ordering = ['-my_field_name']

	def get_absolute_url(self):
		#Returns the url to access a particular instance of MyModuleName
		return reverse('model-detail-view', args = [str(self.id)])
		
	def __str__(self):
		return self.my_field_name

record_1 = MyModelName(my_field_name = "instance_1")
record_1.save()
'''
class Genre(models.Model):
	name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN number</a>')
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

	def display_genre(self):
		return ', '.join(genre.name for genre in self.genre.all()[:3])
	display_genre.short_description = 'Genre'

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

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
		return '{0} ({1})'.format(self.id,self.book.title)
		#return self.book

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
		return '{0} {1}'.format(self.last_name, self.first_name)
		#return self.last_name

class Sign_up(models.Model):
	name = models.CharField(max_length = 20)
	#email_id = models.TextField(email)
	#password = models.TextField(min_legth = 5)


