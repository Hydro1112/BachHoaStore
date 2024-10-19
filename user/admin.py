from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('phone_number', 'email','full_name','last_login','date_joined','is_active')
    list_display_links = ('phone_number', 'full_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.
admin.site.register(User, AccountAdmin)