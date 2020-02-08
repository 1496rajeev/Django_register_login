from django.db import models
from django.contrib.auth.models import User, BaseUserManager

# Create your models here.
class ProfileManager(BaseUserManager):
    pass

class Profile(User):
    objects = ProfileManager()
    class Meta:
        proxy=True
    
