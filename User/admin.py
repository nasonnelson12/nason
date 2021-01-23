from django.contrib import admin

# Register your models here.
from User.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'image_tag']

admin.site.register(UserProfile, UserProfileAdmin)
