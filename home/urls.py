from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index,name='home'),
    path("contact/",views.contact,name="contact"),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('service/',views.service,name='service'),
    path("department",views.department,name="department"),
    path("admindashboard",views.admindashboard,name="admindashboard"),
    path("admindoc",views.admindoc,name="admindoc"),
    path("admin_login",views.Login,name="login"),
    path("logout",views.Logout_admin,name="logout"),
    path("add_doctor",views.add_doctor,name="add_doctor"),
    path("delete_doctor(?P<int:pid>)",views.delete_doctor,name="delete_doctor"),
    path("adminpat",views.adminpat,name="adminpat"),
    path("add_patient",views.add_patient,name="add_patient"),
    path("delete_patient(?P<int:pid>)",views.delete_patient,name="delete_patient"),
    path("admindep",views.admindep,name="admindep"),
    path("add_dep",views.add_dep,name="add_dep"),
]