from django.contrib import admin
from .models import Article, NavLinkModel, FriendLinkModel

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'update_time', 'status']


@admin.register(NavLinkModel)
class NavAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

@admin.register(FriendLinkModel)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

admin.site.site_header = '博客内容管理'
admin.site.site_title = 'Pyloons博客管理'
