from django.contrib import admin
from .models import UserRecipient

class ReceipientAdmin(admin.ModelAdmin):
    list_display = ['user', 'transfer_type', 'bank_name']

admin.site.register(UserRecipient, ReceipientAdmin)
