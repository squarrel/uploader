"""Defined views for the uploads app."""

from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import FileUploadParser, \
    FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from uploads.models import Document
from uploads.serializers import DocumentSerializer
import magic


class DocumentView(APIView):
    """Basic actions for the Document model."""
    parser_classes = (FormParser, MultiPartParser,)#(FileUploadParser,)

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #print('\nrequest.data-->', request.data)
        filename = request.data['filename']
        #print(filename)

        # security check of the uploaded file
        filetype = magic.from_buffer(filename.read())
        #print('\nfiletype-->', filetype)
        allowed_filetypes = [
            'application/pdf', 'ASCII text', 'text/plain']
        if filetype not in allowed_filetypes:
            return Response(status=400)

        serializer = DocumentSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=400)

    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
