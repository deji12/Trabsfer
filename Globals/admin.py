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
    list_display = ('site_name', 'nigerian_bank_name', 'nigerian_bank_account_holder_name', 'nigerian_bank_account_number', 'russian_bank_name', 'russian_bank_account_holder_name', 'russian_card_number', 'russian_phone_number')

admin.site.register(SiteInformation, SiteInformationAdmin)