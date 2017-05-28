from django.db import models
from zinnia.models.entry import Entry

# Create your models here.
class Facebook(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    post_link = models.CharField(max_length=255)