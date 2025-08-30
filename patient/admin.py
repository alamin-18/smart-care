from django.contrib import admin
from .models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'phone', 'address', 'date_of_birth']
    
    def user_full_name(self, obj):
        return obj.user.get_full_name()
admin.site.register(Patient, PatientAdmin)