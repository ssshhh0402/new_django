from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login # login이라는 함수 우리가 정의해서 쓰고있어서 헷갈리지않게 이름 변경


# Create your views here.

# articles할 때는 모델 정의 -> 모델폼 -> create 로직 이었는데
# accounts 관련 로직이 있어서 그걸 활용할거고 UserCreationForm이야
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

# 로그인은 인증과 관련된 폼, Authentication
def login(request):
    if request.method == 'POST':
        # authen-form 은 모델폼이 아니라 인자 순서가 다음과 같이 다르고, request는 그럼 왜 넣느냐. request에 정보가 다 담겨있기 때문이지.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 함수 호출
            user = form.get_user()
            auth_login(request, user)
            # 또는 위의 두 줄을 합쳐서
            # auth_login(request, form.get_user()) 처럼 써도 오키
            return redirect('articles:index')   
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

