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
    """Test all views for the uploads app."""
    def setUp(self):
        self.user = User.objects.create_user(
            'john', password='password', email='john@example.com')

    def tearDown(self):
        os.remove(self.filepath)

    def post_dict(self):
        filepath = self.filepath = os.getcwd() + '/temp_file'
        fw = open(filepath, 'w')
        fw.write('John Doe Biography\n')
        fw.close()
        fo = open(filepath, 'rb')
        post_dict = {
            'name': 'John Doe CV',
            'filename': fo}
        return post_dict
        
    def test_post_method(self):
        #doc = SimpleUploadedFile('CV.pdf', self.create_file, content_type='application/pdf')
        response = self.client.post(reverse('documents'), self.post_dict(), format='multipart')
        print('###')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
