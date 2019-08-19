from django.contrib import admin

# Register your models here.  # 너의 모델을 등록해라
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)