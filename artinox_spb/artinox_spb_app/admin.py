from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('block_name', 'content_text'[:20], 'creation_date', 'moderation_date')
    list_display_links = ('block_name',) #Добавить block_id и генерировать ссылки на необходимый блок
    search_fields = ('block_name', 'content_text')

class PageContentInLine(admin.StackedInline):
    model = PageContent

@admin.register(PageInfo)
class AllPageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title',)
    list_display_links = ('page_name','title',)
    inlines = [PageContentInLine]
