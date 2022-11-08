from django.contrib import admin
from .models import Packages

# Register your models here.
class PackagesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'duration',
    )

    ordering = ('-price',)

admin.site.register(Packages, PackagesAdmin)
