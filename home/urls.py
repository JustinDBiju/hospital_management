from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index,name='home'),
    path("contact/",views.contact,name="contact"),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('service/',views.service,name='service'),
    path("department",views.department,name="department")
]