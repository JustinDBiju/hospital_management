from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Department,Doctor,Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .forms import BookingForm
# Create your views here.
def index(request):
    
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")




def booking(request):
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form ={
        'form':form
    }
    return render(request,"booking.html",dict_form)


def service(request):
    dict_doct={
        'doctor': Doctor.objects.all()
    }
    return render(request,"service.html",dict_doct)


def department(request):
    dict_dept={
        'dept': Department.objects.all()
    }
    return render(request,"department.html",dict_dept)


# admin section views

def admindashboard(request):
    if not request.user.is_staff:
        return redirect("login")
    doctors=Doctor.objects.all()
    patient=Booking.objects.all()
    department=Department.objects.all()

    d=0;
    p=0;
    de=0;
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in department:
        de+=1

    d1={"d":d,'p':p,'de':de}


    return render(request,"admindashboard.html",d1)

def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error='yes'
    d={"error":error}    
    return render(request,"login.html",d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect("home")





def admindoc(request):
    if not request.user.is_staff:
        return redirect("login")
    dict_doct={"doc": Doctor.objects.all()}
    return render(request,"admindoc.html",dict_doct)


def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect("login")
    if request.method=='POST':
        n=request.POST['doct_name']
        s=request.POST['doct_spec']
        d=request.POST['dep_name']
        i=request.POST['doct_img']
        
        try:
            Doctor.objects.create(doct_name=n,doct_spec=s,dep_name=d,doct_img=i)
            error="no"
            
        except:
            error='yes'
    d={"error":error}    
    return render(request,"add_doctor.html",d)


def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect("login")
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('admindoc')

def adminpat(request):
    if not request.user.is_staff:
        return redirect("login")
    dict_doct={"pat": Booking.objects.all()}
    return render(request,"adminpat.html",dict_doct)

def add_patient(request):
    error=""
    if not request.user.is_staff:
        return redirect("login")
    if request.method=='POST':
        n=request.POST['p_name']
        p=request.POST['p_phone']
        e=request.POST['p_email']
        d=request.POST['doct_name']
        bd=request.POST['booking_date']
        
        try:
            Booking.objects.create(p_name=n,p_phone=p,p_email=e,doct_name=d,booking_date=bd)
            error="no"
            
        except:
            error='yes'
    d={"error":error}    
    return render(request,"add_patient.html",d)

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect("login")
    patient = Booking.objects.get(id=pid)
    patient.delete()
    return redirect('adminpat')


def admindep(request):
    if not request.user.is_staff:
        return redirect("login")
    dict_dep={"pat": Department.objects.all()}
    return render(request,"admindep.html",dict_dep)


def add_dep(request):
    error=""
    if not request.user.is_staff:
        return redirect("login")
    if request.method=='POST':
        n=request.POST['dept_name']
        d=request.POST['dept_descrption']
        
        
        try:
            Department.objects.create(dept_name=n,dept_descrption=d)
            error="no"
            
        except:
            error='yes'
    d={"error":error}    
    return render(request,"add_dep.html",d)