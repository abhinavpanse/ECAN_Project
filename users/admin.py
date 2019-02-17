from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser,Profile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display=['username','age','discount_code','email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
