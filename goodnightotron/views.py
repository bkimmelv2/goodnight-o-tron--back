from django.shortcuts import render
from .models import Book, Note
from rest_framework import viewsets, permissions
from .serializers import BookSerializer, NoteSerializer
from django.core.serializers import serialize
from django.views import View
import random
import json
from django.http import JsonResponse

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]

class RandomView(View):
    def get(self, request):
        books = list(Book.objects.all())
        random_books = random.sample(books, 2)
        finalData = json.loads(serialize('json', random_books))
        return JsonResponse(finalData, safe=False)