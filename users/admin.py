from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users import models


class CustomUserAdmin(UserAdmin):
    model = get_user_model()


admin.site.register(models.CustomUser, CustomUserAdmin)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}