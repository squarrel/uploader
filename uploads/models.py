from django.contrib.auth.models import User
from django.db import models
from uploads.utils import set_path


class Document(models.Model):
    """File path of the uploaded file and its related descriptive fields."""
    name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    uploader = models.ForeignKey(User, null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    filename = models.FileField(upload_to=set_path, null=True)

    def __str__(self):
        return self.name
