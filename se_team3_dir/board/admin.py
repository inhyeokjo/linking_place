from django.contrib import admin
from .models import *

# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['place_address', 'place_category']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'reservation_time']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'review_text']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Review, ReviewAdmin)
