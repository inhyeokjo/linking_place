from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_frame),
    path("studyroom", views.category_studyroom),
    path("contents_not_ready", views.contents_not_ready),
    path("post", views.post),
]
