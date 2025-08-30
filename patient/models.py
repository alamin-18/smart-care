from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imges = models.ImageField(upload_to='patients/images')
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.user.get_full_name()
