from api.models import Note
from django.test import TestCase


class NoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        return Note.objects.create(title='title', body='this is body');

    def testTitleContent(self):
        note = Note.objects.get(id=1)
        expected = f'{note.title}'
        self.assertEqual(expected, 'title')

    def testBodyContent(self):
        note = Note.objects.get(id=1)
        expected = f'{note.body}'
        self.assertEqual(expected, 'this is body')