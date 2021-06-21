from django.contrib import admin
from .models import Seuser

# Register your models here.

"""
    <관리자 페이지>
    사용자 정보에 대한 관리자 페이지로 기본적으로 사용자 이름, 사용자 아이디, 패스워드를 볼 수 있도록 설정
"""
class SeuserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_id', 'password']


admin.site.register(Seuser, SeuserAdmin)
