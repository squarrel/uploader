from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from uploads.models import Document
import os

class CreatingDocument(TestCase):
    """Test creating a Document."""
    def setUp(self):
        Document.objects.create(
                name='John Doe CV',
                description='Work biography of John Doe')

    def test_document_created(self):
        document = Document.objects.get(pk=1)
        self.assertEqual(document.name, 'John Doe CV')


class DocumentViewActions(TestCase):
    """Test DocumentView."""
    def setUp(self):
        """Create a user and log her in. Create a file and open it."""
        self.user = User.objects.create_user(
            'john', password='password', email='john@example.com')
        self.client.login(username='john', password='password')

        filepath = self.filepath = os.getcwd() + '/temp_file'
        fw = open(filepath, 'w')
        fw.write('John Doe Biography\n')
        fw.close()
        self.fo = open(filepath, 'rb')

    def tearDown(self):
        """Remove the created file and uploaded file."""
        os.remove(self.filepath)
        try:
            os.remove(self.document.filename.path)
        except:
            pass

    def post_dict(self):
        """Create a dictionary to be sent in a post request."""
        post_dict = {
            'name': 'John Doe CV',
            'filename': self.fo}
        return post_dict
        
    def test_post_method_valid(self):
        """Test view post method by sending it a valid file."""
        response = self.client.post(
            reverse('documents'),
            self.post_dict(),)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        documents = Document.objects.all()
        self.assertEqual(documents.count(), 1)
        document = self.document = documents[0]
        self.assertEqual(document.name, 'John Doe CV')
        self.assertEqual(document.uploader, self.user)
        self.assertTrue(document.filename)

    def test_post_method_error(self):
        response = self.client.post(
            reverse('documents'),
            {},)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
