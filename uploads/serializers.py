"""Serializers for the uploads application models."""
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
        pass
