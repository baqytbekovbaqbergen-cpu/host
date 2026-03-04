from django.contrib import admin
from .models import Articles,Author

@admin.register(Articles,)
class Articlesadmin(admin.ModelAdmin):
    list_display = ('title', 'author')
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("text",)