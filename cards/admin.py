from django.contrib import admin
from cards.models import Cards

class CardsAdmin(admin.ModelAdmin):
    list_display=("cards_heading","cards_title","cards_des","cards_link","cards_image")


admin.site.register(Cards,CardsAdmin)

# Register your models here.
