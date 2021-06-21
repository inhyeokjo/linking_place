"""se_team3_dir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import urls
from django.contrib import admin
from django.urls import path, include
from se_team3_dir import settings
from django.conf.urls.static import static

"""
    접근할 수 있는 url 목록을 나열합니다.
    admin : 관리자 페이지 url
    seuser : 사용자 관련 url
    "" : 메인 화면의 url (127.0.0.1:8000)
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('seuser/', include('seuser.urls')),
    path('', include('board.urls'))
]



