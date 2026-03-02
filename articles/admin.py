from django.contrib import admin
from .models import Articles

@admin.register(Articles)
class Articlesadmin(admin.ModelAdmin):
    list_display = ('title', 'author')
