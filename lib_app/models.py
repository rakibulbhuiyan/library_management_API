from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class User(AbstractUser):
    penalty_points = models.IntegerField(default=0)

class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.due_date = timezone.now().date() + timedelta(days=14)
        super().save(*args, **kwargs)