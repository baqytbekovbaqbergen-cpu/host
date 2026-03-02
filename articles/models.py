from django.db import models
from django.contrib import admin

class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
            return self.title