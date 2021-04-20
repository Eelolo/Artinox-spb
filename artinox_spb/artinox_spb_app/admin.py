from django.contrib import admin

from .models import *
# Register your models here.

class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page', 'block_name', 'content_text'[:20], 'creation_date', 'moderation_date')
    list_display_links = ('page', 'block_name') #Добавить block_id и генерировать ссылки на необходимый блок
    search_fields = ('block_name', 'content_text')


admin.site.register(PageContent, PageContentAdmin)