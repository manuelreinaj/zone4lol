from django.contrib import admin
from foro.models import *

class ForoInline(admin.StackedInline):
    model = Post
class ForoAdmin(admin.ModelAdmin):
    list_filter=['nombre']
    ordering=['-created']
    list_per_page=5
    inlines=[ForoInline]
    readonly_fields = ['created']
    search_fields = ['nombre']

admin.site.register(Foro,ForoAdmin)
admin.site.register(Post)