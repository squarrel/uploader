"""Views for the uploads app."""
from django.http import Http404

from rest_framework import status
from rest_framework.parsers import FileUploadParser, \
    FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from uploads.models import Document
from uploads.serializers import DocumentSerializer


class DocumentList(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetail(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            if 'filename' in request.data:
                serializer.save(
                    uploader=request.user,
                    filename=request.data['filename'])
            else:
                serializer.save(uploader=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
