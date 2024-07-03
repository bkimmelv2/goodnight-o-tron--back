from .models import Book, Note
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Book Serializer
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model to be serialized
        model = Book
        # output fields
        fields = ['id', 'title', 'image']

# Note Serializer
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model to be serialized
        model = Note
        # output fields
        fields = ['id', 'book', 'date', 'text', 'score']