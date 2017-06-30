"""Defined views for the uploads app."""
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import FileUploadParser, \
    FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from uploads.models import Document
from uploads.serializers import DocumentSerializer


class DocumentView(APIView):
    """Basic actions for the Document model."""
    parser_classes = (MultiPartParser, FormParser,)

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
        serializer = DocumentSerializer(
            data=request.data,
            partial=True)

        if serializer.is_valid():
            if 'filename' in request.data:
                serializer.save(
                    uploader=request.user,
                    filename=request.data['filename'])
            else:
                serializer.save(uploader=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_ERROR)

    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
