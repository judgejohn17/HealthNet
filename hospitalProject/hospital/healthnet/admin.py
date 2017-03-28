from django.contrib import admin
from .models import ScheduleItem, Appointment, LogItem, Hospital, Patient, HospitalAdministrator, Doctor, Nurse, \
    InsurancePlan, Drug, Condition, Diagnosis, Prescription, TestResult
from .forms import CreateHospitalAdministratorForm, CreateDoctorForm, CreateNurseForm, CreatePatientForm, PatientForm,\
    NurseForm, DoctorForm, HospitalAdministratorForm


class HealthnetUserAdmin(admin.ModelAdmin):
    """
    Base class for all Healthnet UserAdmin classes to inherit. save_model
    method is overridden to hash input passwords the first time
    a user is created. get_form is overridden to use the add_form when a new
    user is created and the edit_form whenever a user is edited.

    All inheriting classes should specify an add_form and an edit_form.
    """

    add_form = CreatePatientForm
    edit_form = PatientForm

    def save_model(self, request, obj, form, change):
        """
        Hashes the given password if a new user is being created.
        """
        #if the object being handled is new
        if not change:
            #hash the input password
            obj.set_password(form.instance.password)

        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """
        Use add_form during user creation and edit_form for editing users
        """
        defaults = {}
        if obj is None:
            return self.add_form
        else:
            return self.edit_form


class PatientAdmin(HealthnetUserAdmin):
    """
    Admin site functionality for Patients
    """
    add_form = CreatePatientForm
    edit_form = PatientForm


class NurseAdmin(HealthnetUserAdmin):
    """
    Admin site functionality for Nurses
    """
    add_form = CreateNurseForm
    edit_form = NurseForm


class DoctorAdmin(HealthnetUserAdmin):
    """
    Admin site functionality for Doctors
    """
    add_form = CreateDoctorForm
    edit_form = DoctorForm


class HospitalAdministratorAdmin(HealthnetUserAdmin):
    """
    Admin site functionality for Hospital Administrators
    """
    add_form = CreateHospitalAdministratorForm
    edit_form = HospitalAdministratorForm


# Models accessible from the admin site
admin.site.register(ScheduleItem)
admin.site.register(Appointment)
admin.site.register(LogItem)
admin.site.register(Hospital)
admin.site.register(Patient, PatientAdmin)
admin.site.register(HospitalAdministrator,HospitalAdministratorAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Nurse,NurseAdmin)
admin.site.register(InsurancePlan)
admin.site.register(Drug)
admin.site.register(Condition)
admin.site.register(Diagnosis)
admin.site.register(Prescription)
admin.site.register(TestResult)
