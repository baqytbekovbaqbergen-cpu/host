from django.contrib import admin
from .models import Question,Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets =[
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "pub_date","was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "votes"]

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)