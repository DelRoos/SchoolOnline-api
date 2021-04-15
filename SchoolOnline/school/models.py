from enum import unique
from django.db import models
from users.models import NewUser

# Create your models here.
class Speciality(models.Model):
    letter = models.CharField(max_length=10, unique=True)
    describe = models.TextField(blank=True)
    
class Level(models.Model):
    num = models.IntegerField(unique=True)
    describe = models.TextField(blank=True)
    
class Classe(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='spec_class')

class ClassRoom(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name="classroom_user") 
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="classroom_classe") 
    
class Matter(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='class_matter')
    credit = models.IntegerField()   