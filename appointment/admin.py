from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'doctor_name', 
        'patient_name', 
        'appointment_type',  
        'status',            
        'symptoms', 
        'time', 
        'cancel', 
        'created_at'
    ]
    
    def doctor_name(self, obj):
        return obj.doctor.user.get_full_name()
    
    def patient_name(self, obj):
        return obj.patient.user.get_full_name()
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.cancel:
            # Logic to send cancellation email to patient
            subject = 'Appointment Cancellation'
            email_body = render_to_string('appointment_cancellation_email.html', {
                'patient_name': obj.patient.user.get_full_name(),
                'doctor_name': obj.doctor.user.get_full_name(),
                'appointment_date': obj.time.date,
                'appointment_time': obj.time.start_time,
            })
            email = EmailMultiAlternatives(subject, email_body, to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
        if obj.status == 'Running' and obj.appointment_type == 'Online':
            # Logic to send meet link email to patient
            subject = 'Your Online Appointment is Starting'
            email_body = render_to_string('appointment_meet_link_email.html', {
                'patient_name': obj.patient.user.get_full_name(),
                'doctor_name': obj.doctor.user.get_full_name(),
                'appointment_date': obj.time.date,
                'appointment_time': obj.time.start_time,
                'meet_link': obj.doctor.meet_link,
            })
            email = EmailMultiAlternatives(subject, email_body, to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            

admin.site.register(Appointment, AppointmentAdmin)