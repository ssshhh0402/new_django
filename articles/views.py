from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    # articles = Article.objects.all()[0:10] 
    articles = Article.objects.order_by('-id') # 작성
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article.objects.create(title=title, content=content)
    context = {
        'article': article
    }
    # return render(request, 'articles/create.html', context)    
    return redirect(f'/articles/{article.pk}/')  # redirect : 모든 view가 html파일을 가질 필요는 없어! 이렇게 바로 어딘가로 보낼수가 있거든

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)    
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()

    return redirect(f'/articles/{article.pk}/')