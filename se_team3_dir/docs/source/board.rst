board 패키지
===========

* board는 메인화면, 카테고리별 화면에 대한 관리를 수행합니다.
* 메인화면은 여러 카테고리의 페이지를 균형있게 보여줍니다.
* 카테고리별 화면은 특정 카테고리에 대한 목록만 보여줍니다.


board패키지의 admin.py 모듈
------------------
* board의 admin은 관리자페이지에서 보여줄 데이터베이스의 종류를 정의합니다.
  
관리자는 장소의 주소(place_address), 장소의 카테고리(place_category)를 볼 수 있습니다.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

장소 관리::

   class PlaceAdmin(admin.ModelAdmin):
      list_display = ['place_address', 'place_category']

관리자는 예약 데이터베이스에서 예약한 사용자, 예약 시간을 볼 수 있습니다.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
예약 관리::

   class ReservationAdmin(admin.ModelAdmin):
      list_display = ['user', 'reservation_time']

관리자는 리뷰 데이터베이스에서 리뷰를 남긴 사용자와 리뷰 텍스트를 볼 수 있습니다.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
리뷰 관리::

   class ReviewAdmin(admin.ModelAdmin):
      list_display = ['user', 'review_text']

.. automodule:: board.admin
   :members:
   :undoc-members:
   :show-inheritance:


board패키지의 models.py 모듈
-------------------
장소, 예약, 리뷰에 대한 데이터베이스를 djangodb 라이브러리를 이용하여 구현해주는 모듈
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
(djangodb : 클래스를 생성하면 sqlite3를 이용한 데이터베이스 구축을 자동화해주는 라이브러리)

장소 테이블
++++++++
* 장소 테이블에는 장소 주소, 장소 카테고리, 장소 연락처, 장소 이름, 장소 옵션, 장소 설명, 장소 이미지 컬럼이 존재합니다.
* 장고를 이용한 장소 데이터 베이스 구현은 다음과 같습니다.

Place::

   class Place(models.Model):
      """
      장소 주소, 장소 카테고리, 장소 연락처, 장소 이름, 장소 옵션, 장소 설명, 장소 이미지
      """
      place_address = models.CharField(max_length=1000)
      place_category = models.CharField(max_length=200)
      place_contact = models.CharField(max_length=200)
      place_name = models.CharField(max_length=200)
      place_options = models.CharField(max_length=1000)
      place_description = models.CharField(max_length=1000)
      place_image = models.ImageField(upload_to="")

      class Meta:
         db_table = 'linking_space_places'
         verbose_name = '링킹 스페이스 장소'
         verbose_name_plural = '링킹 스페이스 장소'

      def __str__(self):
         return self.place_name

예약 테이블
++++++++
* 예약 테이블에는 예약한 사용자, 예약 장소, 예약 시간, 지불 정보 칼럼이 존재합니다.
* 장고를 이용한 예약 데이터 베이스 구현은 다음과 같습니다.

Reservation::

   class Reservation(models.Model):
      """
      예약한 사용자, 예약 장소, 예약 시간, 지불 정보
      """
      user = models.ForeignKey('seuser.Seuser', on_delete=models.CASCADE)
      place = models.ForeignKey('board.Place', on_delete=models.CASCADE)
      reservation_time = models.CharField(max_length=200)
      payment_info = models.CharField(max_length=1000)

      def __str__(self):
         return self.reservation_time
      
      class Meta:
         db_table = 'linking_space_reservations'
         verbose_name = '링킹 스페이스 예약'
         verbose_name_plural = '링킹 스페이스 예약'

리뷰 테이블
++++++++
* 리뷰 테이블에는 리뷰를 작성한 사용자, 리뷰한 장쇼, 리뷰 작성 시간, 리뷰 텍스트 칼럼이 존재합니다.
* 장고를 이용한 리뷰 데이터 베이스 구현은 다음과 같습니다.

Review::

   class Review(models.Model):
      """
      리뷰를 작성한 사용자, 리뷰한 장소, 리뷰 작성 시간, 리뷰 텍스트
      """
      user = models.ForeignKey('seuser.Seuser', on_delete=models.CASCADE)
      place = models.ForeignKey('board.Place', on_delete=models.CASCADE)
      review_written_time = models.DateTimeField(auto_now=True)
      review_text = models.CharField(max_length=1000)
      # review_image = models.ImageField()
      
      class Meta:
         db_table = 'linking_space_reviews'
         verbose_name = '링킹 스페이스 리뷰'
         verbose_name_plural = '링킹 스페이스 리뷰'

      def __str__(self):
         return self.review_text


.. automodule:: board.models
   :members:
   :undoc-members:
   :show-inheritance:


board 패키지의 urls.py 모듈
-----------------
* board 어플리케이션에서 접근할 수 있는 url목록들을 나열합니다.
* studyroom : 스터디룸 카테고리에 해당하는 장소들만 보여주는 페이지
* contents_not_ready : 아직 준비중인 기능을 표현하는 페이지로 리뷰 작성 기능, 예약 기능은 아직 구현하지 않았습니다.
* \"\" : 메인 화면의 url (127.0.0.1:8000)

urlpatterns::

   urlpatterns = [
      path("", views.main_frame),
      path("studyroom", views.category_studyroom),
      path("contents_not_ready", views.contents_not_ready),
      path("post", views.post),
   ]

.. automodule:: board.urls
   :members:
   :undoc-members:
   :show-inheritance:

board패키지의 views.py 모듈
------------------
* 장고에서 views는 로직(구현)을 담당합니다.
* 주화면 보이기 기능, 카테고리별 화면 보이기 기능이 구현되었습니다.

주화면 보이기 기능
--------------
* 주화면에는 선택할 수 있는 카테고리의 목록과, 추천하는 장소의 목록을 보여줍니다.
* 화면 내에서 로그인과 회원가입 버튼을 클릭할 수 있습니다.
* 카테고리 버튼을 클릭하면 해당 카테고리별 화면으로 전환(redirect)됩니다.

구현::

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


카테고리별 화면 보이기 기능
---------------------
* 현재 스터디룸 카테고리만 선택합니다. (나머지 카테고리들은 데이터를 추가할 시 가능합니다.
* 장소 테이블에서 카테고리 칼럼이 스터디룸 장소만 화면을 구성합니다.

구현::

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

준비되지 않은 컨텐츠, 장소 세부화면 보이기 기능은 준비중입니다.
+++++++++++++++++++++++++++++++++++++++++++++++++++++



.. automodule:: board.views
   :members:
   :undoc-members:
   :show-inheritance:


   board.tests module
------------------

.. automodule:: board.tests
   :members:
   :undoc-members:
   :show-inheritance:
   