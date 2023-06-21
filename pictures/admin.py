from django.contrib import admin

from .models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pub_date")
    search_fields = ("title",)
    readonly_fields = ("pub_date",)
    fieldsets = (
        (None, {"fields": ("title", "contents")}),
        ("Date", {"fields": ("pub_date",)}),
    )
