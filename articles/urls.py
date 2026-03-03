from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("articles/<int:pk>/rate/", views.rate_article, name="rate_article"),
]