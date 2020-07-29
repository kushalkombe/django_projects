from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to = 'media/')
    summary = models.CharField(max_length = 50)
    
