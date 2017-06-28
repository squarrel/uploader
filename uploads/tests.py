from django.test import TestCase
from uploads.models import Document


class CreatingDocument(TestCase):
    """Test creating a Document."""
    def setUp(self):
        Document.objects.create(
                name='John Doe CV',
                description='Work biography of John Doe')

    def test_document_created(self):
        document = Document.objects.get(pk=1)
        self.assertEqual(document.name, 'John Doe CV')
