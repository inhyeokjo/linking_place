from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=200, unique=True)
    user_name = models.CharField(max_length=200)
    user_sex = models.CharField(max_length=200, blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    user_address = models.CharField(max_length=200, blank=True, null=True)
    user_interest = models.CharField(max_length=200, blank=True, null=True)

