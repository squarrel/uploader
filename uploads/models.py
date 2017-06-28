from django.auth import User
from django.db import models
from uploads.utils import set_path


class Document(models.Model):
    """File to be uploaded by user and basic description fields."""
    name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    uploader = models.ForeignKey(User, null=True)
    description = models.CharField(max_length=200, blank=True)
    filename = models.FileField(upload_to=set_path, null=True)
