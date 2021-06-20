from django.contrib import admin
from .models import Seuser

# Register your models here.

class SeuserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_id', 'password']


admin.site.register(Seuser, SeuserAdmin)
