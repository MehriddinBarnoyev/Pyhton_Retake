from django.shortcuts import render
from .models import Article, Category

def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/index.html', {'articles': articles, 'categories': categories})

def category_filter(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'news/index.html', {'articles': articles, 'categories': categories})
