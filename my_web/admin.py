from django.contrib import admin
from my_web.models import contact


@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')   