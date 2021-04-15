from django.db import models

# Create your models here.

class Roles(models.Model):
    roleName = models.CharField(max_length = 128, unique =True )
    description = models.TextField()
    role = models.CharField(max_length = 128)
    
class UserProfile(models.Model):
    firstName = models.CharField(max_length = 128)
    lastName = models.CharField(max_length = 128)
    userName = models.CharField(max_length = 128, unique = True)
    description = models.TextField()
    Roles = models.ManyToManyField(Roles)
    

