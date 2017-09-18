import pytest

from django.contrib.auth.models import User
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from uploads.models import Document
from uploads.views import DocumentList, DocumentDetail


def test_document_list_get(db):
    factory = APIRequestFactory()
    url = reverse_lazy('documents')
    request = factory.get(url)
    response = DocumentList.as_view()(request)
    assert response.status_code == 200
