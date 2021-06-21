seuser 패키지
==============

seuser.admin module
-------------------
* **사용자 정보**에 대한 관리자 모듈입니다.
* 사용자 정보에 대한 **관리자 페이지**로 기본적으로 사용자 이름, 사용자 아이디, 패스워드를 볼 수 있도록 설정합니다.

SeuserAdmin 클래스::

   class SeuserAdmin(admin.ModelAdmin):
      list_display = ['user_name', 'user_id', 'password']

   admin.site.register(Seuser, SeuserAdmin)


* 새로운 라인

.. automodule:: seuser.admin
   :members:
   :undoc-members:
   :show-inheritance:

seuser.models module
--------------------
* seuser 어플리케이션에 필요한 데이터베이스를 클래스화하는 모듈입니다.
* 사용자에 대한 데이터베이스를 djangodb 라이브러리를 이용하여 구현
* (djangodb : 클래스를 생성하면 sqlite3를 이용한 데이터베이스 구축을 자동화해주는 라이브러리)
  
Seuser 클래스 (사용자 클래스)::

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


seuser.urls module
------------------

.. automodule:: seuser.urls
   :members:
   :undoc-members:
   :show-inheritance:

seuser.views module
-------------------

.. automodule:: seuser.views
   :members:
   :undoc-members:
   :show-inheritance:



seuser.tests module
-------------------

.. automodule:: seuser.tests
   :members:
   :undoc-members:
   :show-inheritance: