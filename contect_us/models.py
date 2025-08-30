from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    problem = models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
