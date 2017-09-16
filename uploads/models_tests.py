from datetime import datetime
import pytest

from django.contrib.auth.models import User
from django.utils import timezone
from uploads.models import Document


@pytest.fixture
def user(db):
    user = User.objects.create_user(
        username='john',
        first_name='John',
        last_name='Lennon',
        email='lennon@thebeatles.com'
    )
    return user


def test_create_document(user):
    d_name = 'Name of File'
    d_uploader = user
    d_description = 'File description'
    document = Document.objects.create(
        name=d_name,
        uploader=d_uploader,
        description=d_description
    )
    assert document.name == d_name
    assert document.uploader == d_uploader
    assert document.description == d_description
