from django.db import models
import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200)

class Note(models.Model):
    book = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    text = models.TextField()
    score = models.IntegerField()