from django.contrib import admin
from index.models import Article
from index.models import Email


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_date', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category',)[::-1]


admin.site.register(Article, BlogAdmin)
admin.site.register(Email)