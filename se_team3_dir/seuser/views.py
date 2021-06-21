from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호를 암호화할 때 사용하는 함수
from .models import Seuser

"""
    seuser 어플리케이션에 대한 view 모듈로써 로그인과 회원가입에 대한 메소드가 구현되어 있음.
    함수:
    login : 로그인
    register : 
"""

def login(request):
    """
    로그인 요청이 들어왔을 때 페이지를 구성해주는 메소드
    
    parameter : 
        request : 요청 객체
    리턴 : render(request, 'login.html', res_data)
    """
    if request.method == "GET":
        try:
            if request.session['user_id']:
                del request.session['user_id']
                return redirect('/')
        except:
            pass
        return render(request, 'login.html')
    elif request.method == "POST":
        
        user_id = request.POST.get('user_id', None)
        password = request.POST.get('password', None)

        res_data = {}

        try:
            if not (user_id and password):
                res_data['error'] = "모든 값을 입력해야 합니다."
            else:
                seuser = Seuser.objects.get(user_id=user_id)
                if check_password(password, seuser.password):
                    # 비밀번호가 일치하는 경우
                    print("로그인 성공")
                    request.session['user_id'] = seuser.user_id
                    return redirect('/')
                else:
                    #비밀번호가 틀린 경우
                    res_data['error'] = "비밀번호가 틀렸습니다."
        except:
            res_data['error'] = "!!존재하지 않는 아이디입니다.!!" 

        return render(request, 'login.html', res_data)


def register(request):
    """
    회원가입 요청이 들어왔을 때 화면 구성을 하는 메소드
    parameter:
        request : 요청 객체
    """
    if request.method == 'GET': # url을 입력해서 접근하는 경우
        return render(request, 'register.html')
    elif request.method == "POST": # 버튼을 입력해서 POSt하는 경우
        user_name = request.POST.get('user_name', None)
        user_id = request.POST.get('user_id', None)
        user_email = request.POST.get('user_email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        user_age = request.POST.get('user_age', None)
        if not user_age:
            user_age = 0
        user_sex = request.POST.get('user_sex', None)
        user_address = request.POST.get('user_address', None)
        user_interest = request.POST.get('user_intest', None)
        

        # 비밀번호랑 비밀번호 확인이 다를 경우 에러메시지 출력
        res_data = {}
        if password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."

        if Seuser.objects.filter(user_id=user_id).exists():
            res_data['error'] = "이미 존재하는 아이디입니다." 

        if not (user_name and user_id and password and re_password and user_email and user_sex and user_address and user_age):
            res_data['error'] = '모든 값을 입력해야 합니다.'

        else:    
            seuser = Seuser (
                user_name=user_name,
                user_id=user_id,
                password=make_password(password),  # 비밀번호를 암호화하여 저장
                user_email=user_email,
                user_sex=user_sex,
                user_address=user_address,
                user_interest=user_interest,
                user_age=user_age,
            )

            seuser.save()
            return redirect('/')
       
        return render(request, 'register.html', res_data)

