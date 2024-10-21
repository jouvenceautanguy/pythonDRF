from django.db import models

# Create your models here.
class Author (models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birthdate = models.DateField()
    death = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='authors', null=True, blank=True)

    def __str__(self):
        return self.name

class Editor (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    website = models.URLField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='editors', null=True, blank=True)

    def __str__(self):
        return self.name

class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    cover = models.ImageField(upload_to='books', null=True, blank=True)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    language = models.CharField(max_length=50)
    pages = models.IntegerField()
    format = models.CharField(max_length=50)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Copy (models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50)
    acquisition_date = models.DateField()
    localisation = models.CharField(max_length=50)
    availability = models.BooleanField()

    def __str__(self):
        return self.book.title

class Loan (models.Model):
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date_expected = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    remarks = models.TextField()

    def __str__(self):
        return self.copy.book.title

class Comment (models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField()
    note = models.IntegerField()
    visibility = models.BooleanField()
    moderate = models.BooleanField()

    def __str__(self):
        return self.book.title

class Evaluation (models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    evaluation = models.TextField()
    date = models.DateField()
    note = models.IntegerField()
    title = models.CharField(max_length=50)
    recommended = models.BooleanField()

    def __str__(self):
        return self.book.title
