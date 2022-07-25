from django.contrib import admin
from articles.models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display =  ("article_heading","article_title","article_des","article_image")

admin.site.register(Articles,ArticlesAdmin)

