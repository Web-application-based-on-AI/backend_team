from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.
User = get_user_model()

class AccountAdmin(UserAdmin):
    list_display = ('email','full_name','date_created','is_superuser','is_staff','is_active','last_login')
    search_fields = ('email','full_name')
    readonly_fields = ('date_created','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('full_name',)}),
    #     ('Permissions', {'fields': ('is_superuser','is_staff','is_active')}),
    #     ('Important dates', {'fields': ('last_login', 'date_created')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','full_name','is_staff'),
        }),
    )
    ordering = ()


admin.site.register(User, AccountAdmin)
admin.site.unregister(Group)

