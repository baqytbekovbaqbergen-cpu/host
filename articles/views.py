from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Articles

def rate_article(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        rating = int(request.POST.get("rating", 0))
        article.rating = (article.rating * article.votes + rating) / (article.votes + 1)
        article.votes += 1
        article.save()
        return redirect("article_detail", pk=pk)
    return render(request, "articles/rate.html", {"article": article})


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

def rate_article(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        rating = int(request.POST.get("rating", 0))
        article.rating = (article.rating * article.votes + rating) / (article.votes + 1)
        article.votes += 1
        article.save()
        return redirect("article_detail", pk=pk)
    return render(request, "articles/rate.html", {"article": article})
