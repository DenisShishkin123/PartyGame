from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    # list_display = "__all__" - нельзя
    list_display = ["id", "slug", "title"]
    prepopulated_fields = {"slug": ("title",)}
    # prepopulated_fields = {"slug": ("title", "text")}


admin.site.register(Article, ArticleAdmin)



