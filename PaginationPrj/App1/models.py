from django.db import models

# Create your models here.
class Student(models.Model):
    Roll_No = models.IntegerField()
    Name = models.CharField(max_length=20)
