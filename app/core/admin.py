from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
""" 
Custom User ในหน้า admin
https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
"""

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

    # Set fieldsets to control the layout of admin “add” and “change” pages.
    # https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    # เป็นหน้าจอของ admin คลิกที่ user แต่ละอัน สามารถเพิ่ม field เพื่อดูข้อมูลเพิ่มเติมได้
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide,'),
            'fields': ('email', 'password', 'password2'),
        }),
    )


admin.site.register(models.User, UserAdmin)
