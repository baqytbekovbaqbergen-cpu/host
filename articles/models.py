from django.db import models
from django.contrib import admin

class Author(models.Model):
    text = models.CharField(max_length =200)
    def __str__(self):
        return self.text


class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
            return self.title