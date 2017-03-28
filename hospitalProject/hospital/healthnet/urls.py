from . import views
from django.conf.urls import url

urlpatterns = (
    url(r'^$', views.LoginFormView.as_view(success_url="/healthnet/landing"), name='login-form'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^appointmentsJSON', views.send_appointments_as_JSON, name='JSON appointments'),
    url(r'^register/$', views.CreateAccountView.as_view(success_url="/healthnet"), name='create-account'),
    url(r'^register_doctor/$', views.CreateDoctorAccountView.as_view(success_url="/healthnet"),
        name='create-doctor-account'),
    url(r'^register_nurse/$', views.CreateNurseAccountView.as_view(success_url="/healthnet"),
        name='create-nurse-account'),
    url(r'^register_administrator/$', views.CreateAdministratorAccountView.as_view(success_url="/healthnet"),
        name='create-administrator-account'),
    url(r'^showcalendar/$', views.calendar_view, name='calendar'),
    url(r'^log/$', views.activity_log_view, name='activity-log'),
    url(r'^landing/$', views.landing_view, name='landing'),
    url(r'^appointment/$', views.CreateAppointmentView.as_view(success_url="/healthnet/landing"),
        name='create-appointment'),
    url(r'^appointment_employee/$', views.EmployeeCreateAppointmentView.as_view(success_url="/healthnet/landing"),
        name='employee-create-appointment'),
    url(r'^patientlist/$', views.activity_log_view, name='view-patient-list'),
    url(r'^profile_(?P<pk>[0-9]+)/edit/$', views.UpdateProfileView.as_view(success_url="/healthnet/landing"),
        name='update-profile'),
    url(r'^employee_(?P<pk>[0-9]+)/edit/$', views.UpdateEmployeeView.as_view(success_url="/healthnet/landing"),
        name='update-employee'),
    url(r'^profile_(?P<pk>[0-9]+)/$', views.ProfileDetailView.as_view(), name='profile-detail'),
    url(r'^employee_(?P<pk>[0-9]+)/$', views.EmployeeDetailView.as_view(), name='employee-detail'),
    url(r'^send/$', views.send_message, name="send message"),
    url(r'^message/$', views.message_index, name="message index"),

    url(r'^createdrug/$', views.CreateDrugView.as_view(success_url="/healthnet/createprescription"),
        name="create-drug"),
    url(r'^createcondition/$', views.CreateConditionView.as_view(success_url="/healthnet/landing"),
        name="create-condition"),
    url(r'^creatediagnosis/$', views.CreateDiagnosisView.as_view(success_url="/healthnet/landing"),
        name="create-diagnosis"),
    url(r'^createprescription/$', views.CreatePrescriptionView.as_view(success_url="/healthnet/landing"),
        name="create-prescription"),

    url(r'^list_appointments/$', views.list_appointments, name="verify appointment"),
    url(r'^verify/(?P<pk>[0-9]+)/$', views.confirm_appointment, name='verify appointment'),
    url(r'^list_appointments_delete/$', views.list_appointments_delete, name='delete appointment'),
    url(r'^confirm_delete/(?P<pk>[0-9]+)/$', views.DeleteAppointment.as_view(success_url="/healthnet/landing"),
        name='delete appointment'),
    url(r'^list_appointments_patient/$',views.list_appointments_patients,name='delete appointment patient'),
    url(r'^confirm_delete/(?P<pk>[0-9]+)/$',views.DeleteAppointment.as_view(success_url="/healthnet/landing"),
        name='delete appointment patient'),
    url(r'^update_Appointment/(?P<pk>[0-9]+)/$',views.update_Appointment,name='update appointment'),
    url(r'^update_appointment/$', views.update_appointment, name='update Appointment'),
    url(r'^update_Appointment_nurse/(?P<pk>[0-9]+)/$',views.update_Appointment_nurse,name='update appointment Nurse'),
    url(r'^update_appointment_nurse/$', views.update_appointment_nurse, name='update Appointment Nurse'),

    url(r'^statistics/$', views.StatisticsView, name='Statistics'),
    url(r'^medical_information_diagnosis/$', views.MedicalInformationDiagnosisView.as_view(),
        name='medical-information-diagnosis'),
    url(r'^medical_information_prescription/$', views.MedicalInformationPrescriptionView.as_view(),
        name='medical-information-prescription'),
    url(r'^medical_information_testresult/$', views.MedicalInformationTestResultView.as_view(),
        name='medical-information-testresult'),
    url(r'^deleteprescription/$', views.deleteprescription, name='list-prescriptions'),
    url(r'^confirm_delete_prescription/(?P<pk>[0-9]+)/$', views.DeletePrescription.as_view(success_url="/healthnet/landing"),
        name='delete-prescription'),
    url(r'^admit/([0-9]+)/([0-9]+)$', views.admit_patient_view, name='admit-patient'),
    url(r'^discharge/([0-9]+)/$', views.discharge_patient_view, name='discharge-patient'),
    url(r'^transfer/([0-9]+)/([0-9]+)$', views.transfer_patient_view, name='transfer-patient'),
    url(r'^access_denied', views.admit_patient_view, name='access-denied'),
    url(r'^create_test_results', views.CreateTestResultsView.as_view(success_url="/healthnet/landing"), name='create-test-results'),
    url(r'^all_patients_list/$', views.AllPatientListView.as_view(), name='view-patient-list'),
    url(r'^doctor_list/$', views.DoctorListView.as_view(), name='view-doctor-list')
)