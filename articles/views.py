from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all() # 작성
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)