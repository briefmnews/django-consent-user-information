from django.db import models
from django.conf import settings


class ConsentUserInformation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE
    )
    ip = models.GenericIPAddressField(null=True, blank=True)
    device = models.CharField(max_length=100, blank=True)
    browser = models.CharField(max_length=255, blank=True)
    os = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
