from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호를 암호화할 때 사용하는 함수
from .models import *
from seuser.models import Seuser


def main_frame(request):
    if request.method == "GET":
        res_data = {}
        
        place_instances = Place.objects.values()
        
        for i in range(11):
            res_data['image' + str(i+1)] = place_instances[i]['place_image']
            res_data['desc' + str(i+1)] = place_instances[i]['place_description']
            res_data['name' + str(i+1)] = place_instances[i]['place_name']

        user_id = request.session.get('user_id')
        if user_id:
            user = Seuser.objects.get(user_id=user_id)
            res_data['login'] = user.user_name + "님 안녕하세요!"
            res_data['register'] = ""
            res_data['logout'] = "로그아웃"
        
        else:
            res_data['login'] = "로그인"
            res_data['register'] = "회원가입"
            res_data['logout'] = ""

        return render(request, 'main.html', res_data)
    
    if request.method == "POST":
        request.POST.get()
        return