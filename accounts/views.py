from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login # login이라는 함수 우리가 정의해서 쓰고있어서 헷갈리지않게 이름 변경
from django.contrib.auth import logout as auth_logout
from IPython import embed


# Create your views here.

# articles할 때는 모델 정의 -> 모델폼 -> create 로직 이었는데
# accounts 관련 로직이 있어서 그걸 활용할거고 UserCreationForm이야
def signup(request):
    # 로그인되어있는 사람이 회원가입하려할때 돌려보내기
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입 후 바로 로그인되는 사이트의 방법
            # user = form.save()
            # auth_login(request, user)            
            # 바로 로그인 안되는 사이트
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
    # 로그인되어 있는 사람이 로그인 시도할 때 되돌려 보내기
    if request.user.is_authenticated:
        return redirect('articles:index')    
    if request.method == 'POST':
        # authen-form 은 모델폼이 아니라 인자 순서가 다음과 같이 다르고, request는 그럼 왜 넣느냐. request에 정보가 다 담겨있기 때문이지.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 함수 호출
            user = form.get_user()
            auth_login(request, user)
            # 또는 위의 두 줄을 합쳐서
            # auth_login(request, form.get_user()) 처럼 써도 오키
            # next를 달오고면 앞에꺼, next 안달고.. login 버튼 눌러서 오는거면 뒤에꺼.. 단축평가!
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

