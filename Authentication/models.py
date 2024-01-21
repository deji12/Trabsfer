from django.db import models
from django.contrib.auth.models import User

class UserLoginCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=225)
    date = models.CharField(max_length=225, null=True, blank=True)
    expiration = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return str(self.user)