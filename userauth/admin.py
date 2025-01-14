from django.contrib import admin
from userauth.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from userauth.forms import CustomUserAddForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserAddForm
    form = CustomUserChangeForm
    list_display = ("id", "email", "first_name", "last_name")
    list_filter = ("is_admin", "is_active", "is_superuser", "is_staff")
    readonly_fields = ["created_at", "updated_at", "last_login", "created_by", "uuid"]
    search_fields = ("id", "uuid", "email", "last_name")
    ordering = ("id",)
    fieldsets = (
        (
            "User",
            {
                "fields": (
                    "uuid",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "created_by",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_superuser", "is_admin", "is_staff")},
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "last_login",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password",
                    "confirm_password",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
