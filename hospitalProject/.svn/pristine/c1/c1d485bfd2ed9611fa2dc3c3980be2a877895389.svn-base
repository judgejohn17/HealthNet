from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import ScheduleItem, Patient, Doctor, Nurse, HospitalAdministrator, Message, Drug, Condition, Diagnosis,\
    Prescription, TestResult, TEST_CHOICES


class LoginForm(forms.Form):
    """Form for logging a user in."""
    username = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'Password'}))


class CreatePatientForm(forms.ModelForm):
    """Form for entering info for a new patient"""
    class Meta:
        model = Patient
        fields = ['username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'insurance_plan',
                  'date_of_birth',
                  'phone_number',
                  'doctor',
                  'contact_first_name',
                  'contact_last_name',
                  'contact_phone_number',]
        widgets = {'password': forms.PasswordInput(),
                   'date_of_birth': forms.extras.SelectDateWidget(
                       years=range(1900, 2016)[::-1]),}

    def __init__(self, *args, **kwargs):
        super(CreatePatientForm,self).__init__(*args, **kwargs)
        self.fields['insurance_plan'].label_from_instance = lambda insurance_plan: "%s" % (insurance_plan.name)
        self.fields['doctor'].label_from_instance = lambda doctor: "%s, %s" % (doctor.last_name, doctor.first_name)


class PatientForm(CreatePatientForm):
    """Form for entering patient info"""
    class Meta(CreatePatientForm.Meta):
        exclude = ('password',)


class CreateDoctorForm(forms.ModelForm):
    """Form for entering info for a new Doctor"""
    class Meta:
        model = Doctor
        fields = ['username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'salary',
                  'hospital']
        widgets = {'password': forms.PasswordInput()}

    def __init__(self, *args, **kwargs):
        super(CreateDoctorForm, self).__init__(*args, **kwargs)
        self.fields['hospital'].label_from_instance = lambda hospital: "%s" % (hospital.name)


class DoctorForm(CreateDoctorForm):
    """Form for entering Doctor info"""
    class Meta(CreateDoctorForm.Meta):
        exclude = ('password',)


class CreateNurseForm(forms.ModelForm):
    """Form for entering info for a new Nurse"""
    class Meta:
        model = Nurse
        fields = ['username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'salary']
        widgets = {'password': forms.PasswordInput()}


class NurseForm(CreateNurseForm):
    """Form for entering info for a new Nurse"""
    class Meta(CreateNurseForm.Meta):
        exclude = ('password',)


class CreateHospitalAdministratorForm(forms.ModelForm):
    """Form for entering info for a new Hospital Administrator"""
    class Meta:
        model = HospitalAdministrator
        fields = ['username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'salary',
                  "hospital"]
        widgets = {'password': forms.PasswordInput()}

    def __init__(self, *args, **kwargs):
        super(CreateHospitalAdministratorForm,self).__init__(*args, **kwargs)
        self.fields['hospital'].label_from_instance = lambda hospital: "%s" % (hospital.name)


class HospitalAdministratorForm(CreateHospitalAdministratorForm):
    """Form for entering Hospital Administrator info"""

    class Meta(CreateHospitalAdministratorForm.Meta):
        exclude = ('password',)


class AppointmentForm(forms.ModelForm):
    """Form for patients creating an appointment"""
    class Meta:
        model = ScheduleItem
        fields = ["start_time", "end_time", "description", "doctor"]

    def __init__(self, *args, **kwargs):
        super(AppointmentForm,self).__init__(*args, **kwargs)


class EmployeeAppointmentForm(forms.ModelForm):
    """Form for employees creating a patient appointment"""
    class Meta:
        model = ScheduleItem
        fields = ["start_time", "end_time", "description", "doctor", "person"]

    def __init__(self, *args, **kwargs):
        super(EmployeeAppointmentForm,self).__init__(*args, **kwargs)


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['receiver', 'text',]
        #fields=['receiver','text']


class CreateConditionForm(forms.ModelForm):
    """Form for creating a new condition"""
    class Meta:
        model = Condition
        fields = ['condition_name', ]


class CreateDrugForm(forms.ModelForm):
    """Form for creating a new drug"""

    class Meta:
        model=Drug
        fields = ['drug_name',]


class CreatePrescriptionForm(forms.ModelForm):
    """Form for creating a new prescription"""
    #patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label=None)

    class Meta:
        model=Prescription
        fields = ['doctors_notes','date_prescribed','drug','patient']
        widget = {'date_prescribed': forms.extras.SelectDateWidget(years=range(2016)[::+1]),}

    def __init__(self, *args, **kwargs):
        super(CreatePrescriptionForm,self).__init__(*args, **kwargs)
        self.fields['drug'].label_from_instance = lambda drug: "%s" % drug.drug_name


class CreateDiagnosisForm(forms.ModelForm):
    """Form for creating a new diagnosis"""
    #patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label=None)

    class Meta:
        model=Diagnosis
        fields = ['doctors_notes','condition','date_of_diagnosis','patient']
        widget = {'date_of_diagnosis': forms.extras.SelectDateWidget(years=range(2016)[::+1]), }

    def __init__(self, *args, **kwargs):
        super(CreateDiagnosisForm,self).__init__(*args, **kwargs)
        self.fields['condition'].label_from_instance = lambda condition: "%s" % condition.condition_name


class CreateTestResultsForm (forms.ModelForm):
    """Form for creating test results"""
    #patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label=None)
    #results = forms.CharField(widget=forms.Select(choices=TEST_CHOICES))
    #test_file = forms.FileField()
    #test_image = forms.ImageField()

    class Meta:
        model = TestResult
        fields = ['name','date_of_test','patient','results']
        widget = {'date_of_test': forms.extras.SelectDateWidget(years=range(2016)[::+1]), }

    def __init__(self, *args, **kwargs):
        super(CreateTestResultsForm,self).__init__(*args, **kwargs)
        self.fields['name'].label_from_instance = lambda condition: "%s" % (TestResult.name)


class appointment_update(forms.ModelForm):
    class Meta:
        model=ScheduleItem
        fields=['start_time','end_time','doctor']


class Delete_Appointment(forms.ModelForm):

    class Meta:
        model=ScheduleItem
        fields=["start_time", "end_time", "description","doctor","person"]


class Appointment_Verification(forms.ModelForm):

    class Meta:
        model=ScheduleItem
        fields=['start_time','end_time','verify','accept_appointment']


class Delete_Prescription(forms.ModelForm):

    class Meta:
        model=Prescription
        fields=["drug", "patient", "doctor","doctors_notes","date_prescribed"]
