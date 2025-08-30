from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
# Create your models here.

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
APPOINTMENT_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_TYPES, default='Offline')
    status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default='Pending')
    symptoms = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient.user.get_full_name()} - {self.doctor.user.get_full_name()} - {self.appointment_date} {self.appointment_time}"
