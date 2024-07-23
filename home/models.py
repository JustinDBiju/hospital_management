from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=50)
    dept_descrption=models.TextField()

    def __str__(self):
        return self.dept_name

class Doctor(models.Model):
    doct_name=models.CharField(max_length=50)
    doct_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doct_img=models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr.' + self.doct_name + '- (' + self.doct_spec +')'

class Booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone =models.CharField(max_length=10)
    p_email=models.EmailField(max_length=100)
    doct_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)