from django.db import models
from django.contrib.auth.models import User

class UserRecipient(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=225)

    # nigerian
    account_name = models.CharField(max_length=225, blank=True, null=True)
    account_number  = models.CharField(max_length=225)

    # russian
    phone_number = models.CharField(max_length=225)
    card_number = models.CharField(max_length=225)

    transfer_type = models.CharField(max_length=225)

    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.account_name
