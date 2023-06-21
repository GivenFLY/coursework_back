from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pub_date")
    search_fields = ("title",)
    readonly_fields = ("pub_date",)
    fieldsets = (
        (None, {"fields": ("title", "body", "picture", "access_path")}),
        ("Date", {"fields": ("pub_date",)}),
    )
