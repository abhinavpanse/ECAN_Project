from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    discount_code = models.CharField(max_length=20)
    age = models.PositiveIntegerField(null=True, blank=True)
    sales = models.IntegerField(default=0,null=True,blank=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return 'self.user.username'
        
