"""
Django admin customizations.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Integrates with Django translation system
# if we need to change the language of Django
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    # For List View Page
    ordering = ['id']
    list_display = ['email', 'name']

    # For Update/View model page
    fieldsets = (
        (
            None, {
                'fields': ('email', 'password'),
            }
        ),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (
            _('Important dates'), {
                'fields': ('last_login',)
            }
        )
    )
    readonly_fields = ['last_login']

    # For Add/Create model page
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
