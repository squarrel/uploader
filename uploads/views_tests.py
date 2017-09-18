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
