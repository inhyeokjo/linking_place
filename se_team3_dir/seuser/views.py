from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호를 암호화할 때 사용하는 함수
from .models import Seuser

def login(request):
    if request.method == "GET":
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
                    # 세션
                    pass
                else:
                    #비밀번호가 틀린 경우
                    res_data['error'] = "비밀번호가 틀렸습니다."
        except:
            res_data['error'] = "존재하지 않는 아이디입니다." 

    return render(request, 'login.html', res_data)

# Create your views here.
def register(request):

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
       
        return render(request, 'register.html', res_data)

