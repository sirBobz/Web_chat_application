from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, null=True)
    hobby = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username