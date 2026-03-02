from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articles


def article_list(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    return render(request, 'articles/detail.html', {'article': article})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
