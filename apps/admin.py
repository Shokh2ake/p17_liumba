from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from apps.models import Category, Tag, Blog, Comment, User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    list_display = ('custom_image', "username", "email", "first_name", "last_name", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'image')}),
        (
            _("Permissions"),
            {
                'fields': (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def custom_image(self, obj: User):
        return format_html(
            f'<a href="{obj.pk}">'
            f'<img src="{obj.image.url}" width="35" height="35" style="object-fil: cover;"></a>'
        )

    custom_image.short_description = "Image"


@admin.register(Category)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class Admin(admin.ModelAdmin):
    pass
