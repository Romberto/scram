from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from auth_user.models import Profile

admin.site.unregister(User)


class MyUserAdmin(UserAdmin):
    pass


admin.site.register(Profile)
admin.site.register(User, MyUserAdmin)
