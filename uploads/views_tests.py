"""Test documents app views."""
import pytest
import os

from django.contrib.auth.models import User
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from uploads.models import Document
from uploads.views import DocumentList, DocumentDetail


@pytest.fixture
def user(db):
    """Create a user."""
    user = User.objects.create_user(
        username='john',
        first_name='John',
        last_name='Lennon',
        email='lennon@thebeatles'
    )
    return user


@pytest.fixture
def document(db, user):
    """A Document fixture."""
    document = Document.objects.create(
        name='John CV',
        uploader=user,
        description='Mr Lennons biography'
    )
    return document


def test_document_list_get(db):
    factory = APIRequestFactory()
    url = reverse_lazy('documents')
    request = factory.get(url)
    response = DocumentList.as_view()(request)
    assert response.status_code == 200


def test_document_list_post(db, user):
    factory = APIRequestFactory()
    form_data = {
        'name': 'John Doe CV',
        'description': 'Biography'
    }
    url = reverse_lazy('documents')
    request = factory.post(url, form_data)
    request.user = user
    response = DocumentList.as_view()(request)
    assert response.status_code == 201


def test_document_list_post__empty_form_fail(db, user):
    factory = APIRequestFactory()
    form_data = {}
    url = reverse_lazy('documents')
    request = factory.post(url, form_data)
    request.user = user
    response = DocumentList.as_view()(request)
    assert response.status_code == 400


def test_document_detail_get(db, document):
    factory = APIRequestFactory()
    pk = document.id
    url = reverse_lazy('document', args=(pk,))
    request = factory.get(url)
    response = DocumentDetail.as_view()(request, pk)
    assert response.status_code == 200


def test_document_detail_get__fail(db):
    factory = APIRequestFactory()
    pk = 99
    url = reverse_lazy('document', args=(pk,))
    request = factory.get(url)
    response = DocumentDetail.as_view()(request, pk)
    assert response.status_code == 404
