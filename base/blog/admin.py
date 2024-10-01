from django.contrib import admin
from .models import Categori, Post


# Register your models here.
class CategoriAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



admin.site.register(Categori, CategoriAdmin)
admin.site.register(Post, PostAdmin)
