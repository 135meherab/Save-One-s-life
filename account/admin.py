from django.contrib import admin
from .models import UserAccount, UserBloodGroup
# Register your models here.

class AdminUserBloodGroup(admin.ModelAdmin):
    list_display = ['name', 'slug']



admin.site.register(UserBloodGroup, AdminUserBloodGroup)
admin.site.register(UserAccount)
