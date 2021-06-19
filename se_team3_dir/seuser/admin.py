from django.contrib import admin
from .models import Seuser

# Register your models here.

class SeuserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


admin.site.register(Seuser, SeuserAdmin)
