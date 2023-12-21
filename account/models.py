# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    google_uid = models.CharField(max_length=255, blank=True, null=True)
    google_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email
