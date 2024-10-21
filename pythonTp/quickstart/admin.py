
from django.contrib import admin
from .models import Author, Editor, Book, Category, Copy, Loan, Comment, Evaluation

admin.site.register(Author)
admin.site.register(Editor)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Copy)
admin.site.register(Loan)
admin.site.register(Comment)
admin.site.register(Evaluation)
