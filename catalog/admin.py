from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(MyModelName)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	#pass

#@admin.register(Book)
#@admin.register(BookInstance)
class BooksInstanceInline(admin.TabularInline):
  model = BookInstance

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]
	#pass
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
	list_display = ('book', 'status', 'due_back', 'id')
	fieldsets = (
    (None, {
      'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
     	'fields': ('status', 'due_back')
    }),
  )
	#pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)

