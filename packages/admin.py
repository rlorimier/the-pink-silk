from django.contrib import admin
from .models import Packages


class PackagesAdmin(admin.ModelAdmin):
    """ To show only necessary itens on admin panel """

    list_display = (
        'name',
        'price',
        'duration',
    )

    ordering = ('-price',)


admin.site.register(Packages, PackagesAdmin)
