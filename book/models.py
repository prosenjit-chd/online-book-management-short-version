from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    bookId = models.IntegerField(unique=True, default=0)
    bookName = models.CharField(max_length=50, null=True, default=0)
    numberOfBook = models.IntegerField(null=True)
    bookAuthor = models.CharField(max_length=70, null=True, default=0)
    bookPublication = models.CharField(max_length=70, default=0)

    def __str__(self):
        return f"{self.bookId} {self.bookName}"

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Rent(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    date_taken = models.DateTimeField(default=timezone.now, null=True)
    date_delivery = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.user.name