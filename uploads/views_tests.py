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


filepath = os.getcwd() + '/temp_file'


@pytest.fixture
def file():
    """Create a file and open it."""
    fw = open(filepath, 'w')
    fw.write('John Doe Biography\n')
    fw.close()
    fo = open(filepath, 'rb')
    return fo


@pytest.fixture
def file_clean_up():
    """Remove the created file and uploaded file."""
    os.remove(filepath)
    try:
        os.remove(self.document.filename.path)
    except:
        pass
    fo.close()


def test_document_list_get(db):
    factory = APIRequestFactory()
    url = reverse_lazy('documents')
    request = factory.get(url)
    response = DocumentList.as_view()(request)
    assert response.status_code == 200


def test_document_list_post(db, user, file):
    factory = APIRequestFactory()
    form_data = {
        'name': 'John Doe CV',
        'filename': file,
        'description': 'Biography'
    }
    url = reverse_lazy('documents')
    request = factory.get(url, form_data)
    response = DocumentList.as_view()(request)
    assert response.status_code == 201
    file_clean_up()
