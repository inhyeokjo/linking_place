from django.db import models
# Create your models here.

"""
    장소, 예약, 리뷰에 대한 데이터베이스를 djangodb 라이브러리를 이용하여 구현
    (djangodb : 클래스를 생성하면 sqlite3를 이용한 데이터베이스 구축을 자동화해주는 라이브러리)
"""

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

