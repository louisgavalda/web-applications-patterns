from django.contrib import admin

from .models import Book, Borrower, Loan

admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Loan)
