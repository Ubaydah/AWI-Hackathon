from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Creditor ,Profile, \
    Wallet, WalletTransaction


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    readonly_fields = ('created_at', 'updated_at',)
    model = CustomUser
    list_display = ('username', 'email', 'is_staff',
                    'is_active', 'slug', 'created_at', 'updated_at')
    list_filter = ('username', 'email', 'is_staff', 'is_active',
                   'slug', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('username', 'email',
         'password', 'slug', 'created_at', 'updated_at')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'slug', 'created_at', 'updated_at')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class BaseClassAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Creditor, BaseClassAdmin)
admin.site.register(Profile, BaseClassAdmin)
admin.site.register(Wallet, BaseClassAdmin)
admin.site.register(WalletTransaction, BaseClassAdmin)