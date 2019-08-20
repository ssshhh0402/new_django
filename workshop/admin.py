from django.contrib import admin

# Register your models here.

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','birthday','age')
    
admin.site.register(Student,StudentAdmin)

