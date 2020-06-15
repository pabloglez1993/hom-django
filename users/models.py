from django.db import models
from django.contrib.auth.models import User

class Architect(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cell_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.user.user_name}'