from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Availble"), (1, "On Loan"))


class Category(models.Model):
    category_code = models.CharField(max_length=10, unique=True)
    category_description = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.category_code  # or any field you prefer


class Book(models.Model):
    book_code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50, unique=False)
    author = models.CharField(max_length=50, unique=False)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books_in_this_category")
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title  # or any field you prefer