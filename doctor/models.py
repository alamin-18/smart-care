from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=100)
    
    def __str__(self):
        return self.name
class Designation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=100)
    
    def __str__(self):
        return self.name
class AvailableTime(models.Model):
    time = models.CharField(max_length=100)
    
    def __str__(self):
        return self.time
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/images')
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.PositiveIntegerField(help_text="Experience in years" , default=0)
    specialization = models.ManyToManyField(Specialization)
    designation = models.ManyToManyField(Designation)
    available_time = models.ManyToManyField(AvailableTime)
    bio = models.TextField()
    meet_link = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10, choices=STAR_CHOICES)
    
    def __str__(self):
        return f"Review by {self.reviewer.user.get_full_name()} for {self.doctor.user.get_full_name()}"