from django.contrib import admin

from .models import Tag, Note


admin.site.register(Tag)
admin.site.register(Note)
