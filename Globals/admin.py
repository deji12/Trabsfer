from django.contrib import admin
from .models import *

class RateAdmin(admin.ModelAdmin):
    list_display = ['currency_name', 'rate']

admin.site.register(Rate, RateAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'receipient', 'from_currency', 'to_currency', 'amount', 'paid', 'has_receipient', 'date']

admin.site.register(Transaction, TransactionAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'bank_name', 'account_type']

admin.site.register(Account, AccountAdmin)

class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_title', 'facebook_link', 'twitter_link', 'whatsapp_link', 'instagram_link', 'contact_email', 'contact_number')

admin.site.register(SiteInformation, SiteInformationAdmin)