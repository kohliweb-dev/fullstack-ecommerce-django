from django.db import models

# Create your models here.
from django.db import models
from autoslug import AutoSlugField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='blog/')
    slug = AutoSlugField(populate_from ='title',unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title

