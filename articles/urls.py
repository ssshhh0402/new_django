from django.urls import path

from . import views

app_name = 'articles'  #이거를 해줘야 다른 앱에서 같은 name을 써도 내가 원하는 곳으로 갈수있겠지

urlpatterns = [
    path('',views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'),
]


