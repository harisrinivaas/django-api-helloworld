from django.contrib import admin

from app.models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'content')

admin.site.register(Article, ArticleAdmin)
