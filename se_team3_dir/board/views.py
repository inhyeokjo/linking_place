from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호를 암호화할 때 사용하는 함수
from .models import *
from seuser.models import Seuser

"""
    board 어플케이션의 view로써 모델의 로직을 담당한다.
    들어온 요청에 따라 화면을 구성해주는 메소드들을 담고 있다.
    
    함수 목록:
    main_frame : 메인 화면을 구성해주는 함수
    category_studyroom : 카테고리별 화면(스터디 룸) 화면을 구성해주는 함수
    contents_not_ready : 현재 준비중인 서비스를 표시하는 함수 (미완성) 
    post : 각 장소별 세부 화면을 구성해주는 함수 (미완성)
"""

def main_frame(request):
    """
    메인 화면을 구성하는 메소드
    파라미터:
        request : 요청 객체
    리턴 : render(request, main.html, res_data) 
    """
    if request.method == "GET":
        res_data = {}
        
        places_list = ['강의실', '공연장', '운동시설', '카페', '쿠킹 스튜디오', '스터디룸']

        place_instances = Place.objects.values()

        # 장소를 카테고리별로 분류
        place_categorical_dict = {}                     # 키 : 장소 카테고리, value : 장소 객체 리스트
        for i in range(len(places_list)):               # 카테고리 6개이므로 6번 반복
            place_categorical_dict[places_list[i]] = [] 

        for i in range(place_instances.count()):        # 모든 장소를 불러와서 카테고리별로 분류
            for place in places_list:
                if place_instances[i]['place_category'] == place:
                    place_categorical_dict[place].append(place_instances[i])


        # 화면 구성에 필요한 정보들 (장소 이름, 이미지, 세부정보, 주소, 연락처)를 전달하기 위해서 res_data 딕셔너리에 추가
        n = 0
        for j, place in enumerate(places_list):
            for i in range(2):
                res_data['name' + str(n+1)] = place_categorical_dict[place][i]['place_name']
                res_data['image' + str(n+1)] = "../static/img/" + place_categorical_dict[place][i]['place_image']
                res_data['desc' + str(n+1)] = place_categorical_dict[place][i]['place_description']
                res_data['address' + str(i+1)] = place_categorical_dict[place][i]['place_address']
                res_data['contact' + str(i+1)] = place_categorical_dict[place][i]['place_contact']
                n += 1
        
        
        user_id = request.session.get('user_id')        # 세션에 로그인한 사용자 정보가 있다면 로그인된 상태로 표시
        if user_id:
            user = Seuser.objects.get(user_id=user_id)
            res_data['login'] = user.user_name + "님 안녕하세요!"
            res_data['register'] = ""
            res_data['logout'] = "로그아웃"
        
        else:                                           # 세션에 로그인한 사용자 정보가 없다면 로그인 또는 회원가입 할 수 있도록 표시
            res_data['login'] = "로그인"
            res_data['register'] = "회원가입"
            res_data['logout'] = ""

        return render(request, 'main.html', res_data)
    
def category_studyroom(request):
    """
    카테고리별 화면을 구성하는 메소드
    파라미터 : 
        request : 요청 객체
    리턴 : render(request, category, res_data)
    """
    if request.method == "GET":
        res_data = {}
        place_instances = Place.objects.filter(place_category="스터디룸")

        for i, place in enumerate(place_instances):
            res_data['name' + str(i+1)] = place.place_name
            res_data['address' + str(i+1)] = place.place_address
            res_data['image' + str(i+1)] = "../static/img/" + str(place.place_image)
            res_data['description' + str(i+1)] = place.place_description
            res_data['contact' + str(i+1)] = place.place_contact
    
        return render(request, 'studyroom.html', res_data)

    elif request.method == "POST":
        pass
            

def contents_not_ready(request):
    if request.method == "GET":
        res_data = {}
        """
        기능 추가 예정
        """
        for i in range(20):
            res_data['img' + str(i+1)] = "../static/img/ready.gif"
            res_data['address' + str(i+1)] = "준비중입니다..!"
            res_data['image' + str(i+1)] = "준비중입니다..!"
            res_data['description' + str(i+1)] = "준비중입니다..!" 
            res_data['contact' + str(i+1)] = "준비중입니다..!"

        return render(request, 'contents_not_ready.html', res_data)

    elif request.method == "POST":
        pass
        

def post(request):
    """
    기능 추가 예정
    """
    if request.method == "GET":
        return render(request, 'post.html')
    else:
        print("지원하지 않는 서비스입니다.")