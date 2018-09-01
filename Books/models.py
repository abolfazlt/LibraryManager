from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_logo = models.FileField(max_length=500, default='')
    taken_by = models.CharField(max_length=300)  # User's username here if book is taken
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('Books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.author

class RequestedBooks(models.Model):
    title= models.CharField(max_length=100)
    author=models.CharField(max_length=100 , blank=True)
    #publisher=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title+" - "+ self.author

