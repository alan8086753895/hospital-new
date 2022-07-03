from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,covidcase
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
import json 

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)


admin.site.register(covidcase)

class PatientAdmin(admin.ModelAdmin): formfield_overrides = {
    map_fields.AddressField: { "widget":
    map_widgets.GoogleMapsAddressWidget(attrs={
      "data-autocomplete-options": json.dumps({ "types": ["geocode",
      "establishment"], "componentRestrictions": {
                  'country': 'in'
              }
          })
      })
    },
}