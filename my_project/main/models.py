from django.db import models
from datetime import datetime as dt
import os

# Create your models here.
def upload_to(instance, filename):
    # Defina o caminho para o upload das imagens.
    return os.path.join('movies_covers', filename)

class My_movies(models.Model):
    # here we define the columns of our database

    title = models.CharField(max_length=50)
    description = models.TextField()
    year = models.DateField()
    date = models.DateTimeField("Posting date", default=dt.now())
    movie_cover = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title

