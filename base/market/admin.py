from django.contrib import admin

# Register your models here.
from .models import Market


# Register your models here.
class MarketAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Market, MarketAdmin)




