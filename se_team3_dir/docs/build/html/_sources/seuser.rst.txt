seuser 패키지
==============

seuser 패키지의 admin.py 모듈
-------------------
* 사용자 정보에 대한 관리자 모듈입니다.
* 사용자 정보에 대한 관리자 페이지로 기본적으로 사용자 이름, 사용자 아이디, 패스워드를 볼 수 있도록 설정합니다.

SeuserAdmin 클래스::

   class SeuserAdmin(admin.ModelAdmin):
      list_display = ['user_name', 'user_id', 'password']

   admin.site.register(Seuser, SeuserAdmin)


* 새로운 라인

.. automodule:: seuser.admin
   :members:
   :undoc-members:
   :show-inheritance:

seuser 패키지의 models.py 모듈
---------------------------
* seuser 어플리케이션에 필요한 데이터베이스를 클래스화하는 모듈입니다.
* 사용자에 대한 데이터베이스를 djangodb 라이브러리를 이용하여 구현
* (djangodb : 클래스를 생성하면 sqlite3를 이용한 데이터베이스 구축을 자동화해주는 라이브러리)
  
Seuser 테이블 (사용자 데이터베이스)::

   class Seuser(models.Model):
      """
         사용자 이름, 사용자 아이디, 사용자 이메일, 비밀번호,회원 가입 시간,
         사용자 성별, 사용자 나이, 사용자 주소, 사용자 관심사
      """
      user_name = models.CharField(max_length=64, verbose_name='사용자명', default="anonymous")
      user_id = models.CharField(max_length=200, verbose_name="사용자 아이디", default="nouser")
      user_email = models.EmailField(max_length=128, verbose_name='사용자이메일', default="email@none.com")
      password = models.CharField(max_length=64, verbose_name="비밀번호", default="0")
      registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
      user_sex = models.CharField(max_length=200, verbose_name="성별", default="남자")
      user_age = models.IntegerField(verbose_name="나이", default=-1)
      user_address = models.CharField(max_length=200, blank=True, null=True, verbose_name="주소")
      user_interest = models.CharField(max_length=200, blank=True, null=True, verbose_name="사용자 관심사")

      def __str__(self):
         return self.user_name

      class Meta:
         db_table = 'linking_space_seuser'
         verbose_name = '링킹 스페이스 사용자'
         verbose_name_plural = '링킹 스페이스 사용자'
  


.. automodule:: seuser.models
   :members:
   :undoc-members:
   :show-inheritance:


seuser패키지의 urls.py 모듈
------------------------
* seuser 어플리케이션에서 접근할 수 있는 url목록들을 나열합니다.
* admin : 관리자 페이지 url
* seuser : 사용자 관련 url
* \"\" : 메인 화면의 url (127.0.0.1:8000)

필요한 라이브러리 import::

   from django import urls
   from django.contrib import admin
   from django.urls import path, include

urlpatterns::

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('seuser/', include('seuser.urls')),
      path('', include('board.urls'))
   ]


.. automodule:: seuser.urls
   :members:
   :undoc-members:
   :show-inheritance:

seuser 패키지의 views.py 모듈
-------------------
* 장고에서 views는 로직(구현)을 담당합니다.
* 로그인 기능과 회원 가입 기능이 구현되었습니다.

로그인
----
* 로그인은 사용자가 존재하는 아이디와 그에 해당하는 비밀번호를 정상적으로 입력하면 수행됩니다.
* 사용자가 로그인을 수행하면 세션(쿠키)에 값이 저장되어 로그아웃을 하기 전까지 로그인 상태가 유지됩니다.

로그인 코드입니다.::

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

회원가입
------
* 다음은 회원 가입 기능입니다.
* 사용자는 회원 가입을 할 때 모든 정보를 입력하고 기존에 가입된 회원이 아니라면 회원 가입이 수행됩니다.
* 또한 비밀번호와 비밀번호 확인 란이 동일한 문자열을 입력해야 합니다.

회원가입에 대한 코드입니다.::

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

.. automodule:: seuser.views
   :members:
   :undoc-members:
   :show-inheritance:



seuser.tests module
-------------------
* 

.. automodule:: seuser.tests
   :members:
   :undoc-members:
   :show-inheritance: