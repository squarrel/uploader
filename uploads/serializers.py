"""Serializers for the uploads application models."""
from rest_framework import serializers
from uploads.models import Document
import magic


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'name',
            'date',
            'uploader',
            'description',
            'filename'
        )

    def validate_filename(self, filename):
        """Validate type of file."""
        filetype = magic.from_buffer(filename.read())
        allowed_filetypes = [
            'application/pdf', 'ASCII text', 'text/plain']
        if filetype not in allowed_filetypes:
            raise serializers.ValidationError('The file is of unapproved type.')

    def create(self, validated_data):
        return Document.objects.create(**validated_data)
