from django.contrib import admin

from .models import Defib

class DefibAdmin(admin.ModelAdmin):
    pass

admin.site.register(Defib, DefibAdmin)
