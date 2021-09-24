from django.db import models

# Create your models here.
class Three_Mile(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    high_alt = models.CharField(max_length=10)

class Row(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    high_alt = models.CharField(max_length=10)


class Crunches(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    reps = models.CharField(max_length=10)
    score = models.CharField(max_length=10)

class Plank(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    
class Pullups(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    reps = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    
class Pushups(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    reps = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    
    def __str__(self):
        return self.id
