"""Serializers for the uploads application models."""
from rest_framework import serializers
from uploads.models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
                'id',
                'name',
                'date',
                'uploader',
                'description',
                'filename')

    def create(self, validated_data):
        return Document.objects.create(**validated_data)
