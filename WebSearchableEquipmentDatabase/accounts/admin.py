from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account


class AccountAdmin(UserAdmin):
    """Customizes the admin page to display desired information regarding Accounts also sets up filtering ability
        for site admin"""
    model = Account
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'groups', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}),
    # for finer grain control add - , 'user_permissions'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# registers our model and admin
admin.site.register(Account, AccountAdmin)
