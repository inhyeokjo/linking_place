from django.db import models
# Create your models here.

class Place(models.Model):
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

