from django.urls import path
from frondend import views
urlpatterns =[
    path('homehtmlpage/',views.homehtmlpage,name="homehtmlpage"),
    path('aboutuspage/',views.aboutuspage,name="aboutuspage"),
    path('contact/',views.contact,name="contact"),
    path('doctorpage/',views.doctorpage,name="doctorpage"),
    path('displaysingledepart/<itemcatg>/', views.displaysingledepart, name="displaysingledepart"),
    path('savecontactuspage/',views.savecontactuspage,name="savecontactuspage"),
    path('webloginpage/',views.webloginpage,name="webloginpage"),
    path('appointment/',views.appointment,name="appointment"),
    path('savebookdb/',views.savebookdb,name="savebookdb"),
    path('custemerlogin/',views.custemerlogin,name="custemerlogin"),
    path('logout/',views.logout,name="logout"),
    path('docloginpage/',views.docloginpage,name="docloginpage"),
    path('patientlogin/', views.patientlogin, name="patientlogin"),
    path('logoutpatient/', views.logoutpatient, name="logoutpatient"),
    path('bookingpage/',views.bookingpage,name="bookingpage"),
    path('viewbookingfront/',views.viewbookingfront,name="viewbookingfront"),
    path('savecustomer/',views.savecustomer,name="savecustomer"),


]
