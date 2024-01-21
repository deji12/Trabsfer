from django.db import models
from django.contrib.auth.models import User
from Receipient.models import UserRecipient
import uuid

ACCOUNT_TYPE_CHOICES = [
    ("NIGERIAN NAIRA", "Nigerian Naira"),
    ("RUSSIAN ROUBLE", "Russian Rouble")
]

class Rate(models.Model):
    currency_name = models.CharField(max_length=225)
    rate = models.FloatField()

    def __str__(self):
        return self.currency_name
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipient = models.ForeignKey(UserRecipient, on_delete=models.CASCADE, null=True, blank=True)
    from_currency = models.CharField(max_length=225)
    to_currency = models.CharField(max_length=225)
    current_exchange_rate = models.FloatField(max_length=225, null=True, blank=True)
    amount = models.FloatField()
    transaction_id = models.CharField(max_length=225)
    converted_amount = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    has_receipient = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Account(models.Model):
    account_type = models.CharField(max_length=225, choices=ACCOUNT_TYPE_CHOICES)
    bank_name = models.CharField(max_length=225)

    # nigerian
    account_name = models.CharField(max_length=225, blank=True, null=True)
    account_number  = models.CharField(max_length=225)

    # russian
    phone_number = models.CharField(max_length=225)
    card_number = models.CharField(max_length=225)

    def __str__(self):
        return self.account_type
    
from django.contrib.sites.models import Site

class SiteInformation(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=225, null=True, blank=True)
    site_title = models.CharField(max_length=225, null=True, blank=True)

    nigerian_bank_name = models.CharField(max_length=225, null=True, blank=True, help_text="Name of Nigerian bank")
    nigerian_bank_account_holder_name = models.CharField(max_length=225, null=True, blank=True, help_text="Name of nigerian bank account holder")
    nigerian_bank_account_number = models.CharField(max_length=225, null=True, blank=True, help_text="Account number for the nigerian bank account")

    russian_bank_name = models.CharField(max_length=225, null=True, blank=True, help_text="Name of bank")
    russian_bank_account_holder_name = models.CharField(max_length=225, null=True, blank=True, help_text="Name of russian bank account holder")
    russian_card_number = models.CharField(max_length=225, null=True, blank=True, help_text="Card number for the russian bank account")
    russian_phone_number = models.CharField(max_length=225, null=True, blank=True, help_text="Phone number for the russian bank account")

    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=225, blank=True, null=True)
    footer_message = models.TextField(blank=True, null=True)
    contact_page_message = models.TextField(blank=True, null=True)

    