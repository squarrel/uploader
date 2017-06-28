"""Defined views for the uploads app."""

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uploads.models import Document


class DocumentView(views.APIView):
    """Basic actions for the Document model."""
    parser_classes = (FileUploadParser,)

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=true)
        return Response(serializer.data)

    def post(self, request, filename, format=None):
        uploading_file = request.data['file']
        # security check of the uploaded file
        # to do here

        return Response(status=201)

    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
