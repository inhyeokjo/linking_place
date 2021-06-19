from django.db import models

# Create your models here.


class Reservation(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    place = models.ForeignKey('reservation.Place', on_delete=models.CASCADE)
    reservation_time = models.CharField(max_length=200)
    payment_info = models.CharField(max_length=1000)


class Review(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    place = models.ForeignKey('reservation.Place', on_delete=models.CASCADE)
    review_written_time = models.DateTimeField(auto_now=True)
    review_text = models.CharField(max_length=1000)
    # review_image = models.ImageField()


class Place(models.Model):
    place_address = models.CharField(max_length=1000)
    place_category = models.CharField(max_length=200)
    place_contact = models.CharField(max_length=200)
    place_name = models.CharField(max_length=200)
    place_options = models.CharField(max_length=1000)
    place_description = models.CharField(max_length=1000)