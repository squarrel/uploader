from django.contrib import admin
from uploads.models import Document


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('uploader',)

admin.site.register(Document, DocumentAdmin)
