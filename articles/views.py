from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from IPython import embed
from .models import Article
# Create your views here.

def index(request):
    # articles = Article.objects.all()[0:10] 
    # print(request.scheme)
    # print(request.method)
    # print(request.get_host())
    # print(request.get_full_path())
    # print(request.build_absolute_uri()) #이렇게 request 오브젝트에는 다양한 정보가 담겨있다
    articles = Article.objects.order_by('-id') # 작성
    context = {
        'articles': articles
    }
    # embed()
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        context = {
            'article': article
        }
        # return render(request, 'articles/create.html', context)    
        # embed()
        return redirect('articles:detail', article.pk)  # redirect : 모든 view가 html파일을 가질 필요는 없어! 이렇게 바로 어딘가로 보낼수가 있거든
    else:
        return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # else: # 이렇게하면 포스트 요청으로만 지울 수 있으니까 주소창에서 ~/123/delete 이렇게 적는다고 지워지지 않겠지
    #     return redirect('articles:detail', article.pk)

# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)    
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article':article
        }
        return render(request, 'articles/edit.html', context)
