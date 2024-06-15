from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'nickname', 'phone', 'is_staff', 'is_superuser')

    def nickname(self, obj):
        return obj.profile.nickname

    nickname.short_description = '昵称'

    def phone(self, obj):
        return obj.profile.phone

    phone.short_description = '号码'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'phone')
