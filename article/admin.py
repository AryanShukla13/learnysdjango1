from django.contrib import admin
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_icon','article_title','article_des')

admin.site.register(Article,ArticleAdmin)
# Register your models here.
