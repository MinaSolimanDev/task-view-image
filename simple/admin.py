from django.contrib import admin
from .models import Items

class CustomItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'imageUrl', 'created', 'updated',)

admin.site.register(Items, CustomItemsAdmin)