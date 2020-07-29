from django.db import models

# Create your models here.


class Feedback(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=36)
    email = models.EmailField()
    marks = models.FloatField()
    feedback = models.CharField(max_length=50)
