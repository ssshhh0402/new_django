from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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

