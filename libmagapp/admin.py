from django.contrib import admin
from libmagapp.models import Book
from libmagapp.models import BookLending
from libmagapp.models import BookRequest
from libmagapp.models import Member
from libmagapp.models import LibraryCard
from libmagapp.models import Librarian
# Register your models here.

admin.site.register(Book)
admin.site.register(BookLending)
admin.site.register(BookRequest)
admin.site.register(Member)
admin.site.register(LibraryCard)
admin.site.register(Librarian)