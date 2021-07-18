from api.models import Note
from rest_framework import fields, serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'author', 'createdAt', 'updatedAt', 'body', 'likes']