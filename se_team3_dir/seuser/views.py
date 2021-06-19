from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호를 암호화할 때 사용하는 함수
from .models import Seuser

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        else:
            seuser = Seuser.objects.get(username=username)
            if check_password(password, seuser.password):
                # 비밀번호가 일치하는 경우
                # 세션
                # 
                pass
            else:
                #비밀번호가 틀린 경우
                res_data['error'] = "비밀번호가 틀렸습니다."
            

    return render(request, 'login.html', res_data)

# Create your views here.
def register(request):

    if request.method == 'GET': # url을 입력해서 접근하는 경우
        return render(request, 'register.html')
    elif request.method == "POST": # 버튼을 입력해서 POSt하는 경우
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        

        # 비밀번호랑 비밀번호 확인이 다를 경우 에러메시지 출력
        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        if password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."

        else:    
            seuser = Seuser(
                username=username,
                password=make_password(password),  # 비밀번호를 암호화하여 저장
                useremail=useremail
            )
            seuser.save()
       
        return render(request, 'register.html', res_data)