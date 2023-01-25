from django.contrib import admin
from .models import ContentManagmentSystem, SiteData


class CoreDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'created_at')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class ContentManagmentSystemAdmin(admin.ModelAdmin):
    list_display = ('title', )


class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('site_name', )


admin.site.register(ContentManagmentSystem, ContentManagmentSystemAdmin)
admin.site.register(SiteData, SiteDataAdmin)
