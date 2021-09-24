from django.db import models

# Create your models here.
class Movement_Contact(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    time = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    high_alt = models.CharField(max_length=20)

class Maneuver_Fire(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    time = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    high_alt = models.CharField(max_length=20)

class Ammo_Lift(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    reps = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    
    def __str__(self):
        return self.id
    
