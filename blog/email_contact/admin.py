from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    readonly_fields = ('email', )  # поля только для чтения