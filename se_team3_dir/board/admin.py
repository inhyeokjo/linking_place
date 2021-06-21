from django.contrib import admin
from .models import *

"""
    <관리자 페이지>
    장소, 예약, 리뷰에 대한 관리자 페이지로 기본적으로 사용자 이름, 사용자 아이디, 패스워드를 볼 수 있도록 설정
"""

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['place_address', 'place_category']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'reservation_time']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'review_text']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Review, ReviewAdmin)
