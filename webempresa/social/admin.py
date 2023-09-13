from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        # Si el usuario logueado pertenece al grupo personal
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')
            


admin.site.register(Link, LinkAdmin)