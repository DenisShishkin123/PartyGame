from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ["id", "action"]


# admin.site.register(Card)
admin.site.register(Card, CardAdmin)







