from django.contrib import admin
from store.models.user import CustomUser  # Assuming a custom user model

# Registering the User model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'is_active', 'is_staff')
    search_fields = ('username',)
    list_filter = ('is_active', 'is_staff')
    ordering = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional Info', {'fields': ('phone_number',)}),  # Include phone_number in the admin form
    )
