from django.contrib import messages
from django.shortcuts import render, redirect
from backend.models import department, doctor, contactusdb, appointmentdb
from backend.views import displaybook
from frondend.models import deatilescustomer


def homehtmlpage(requst):
    data = department.objects.all()
    return render(requst,"home.html",{'data':data})
def aboutuspage(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request,"contact.html")
def doctorpage(request):
    data = doctor.objects.all()
    return render(request, "doctors.html", {'data': data})
# def singledepartpage(request):
#     return render(request,"singledepartment.html")
def displaysingledepart(request, itemcatg):
    print("===itemcatg===",itemcatg)
    catg = itemcatg.upper()
    products=doctor.objects.filter(Department=itemcatg)
    context={
          'products':products,
            'catg':catg
    }
    return render(request,"singledepartment.html",context)
def savecontactuspage(req):
    if req.method == "POST":
        na = req.POST.get('name')
        eml = req.POST.get('email')
        sub = req.POST.get('subject')
        msg = req.POST.get('message')
        obj=contactusdb(NAME=na, EMAIL=eml, SUBJECT=sub, MESSAGE=msg)
        obj.save()
        return redirect(contact)
def webloginpage(req):
    return render(req,"weblogin.html")
def appointment(request):
    da = department.objects.all()
    return render(request, "appointment.html", {'da': da})
def savebookdb(req):
    if req.method == "POST":
        na = req.POST.get('name')
        eml = req.POST.get('email')
        dep = req.POST.get('departments')
        num = req.POST.get('number')
        dt = req.POST.get('date')
        tm = req.POST.get('time')
        obj=appointmentdb(Name=na,Emailadress=eml,Departmentdb=dep,Phonenumber=num,Date=dt,Time=tm)
        obj.save()
        return redirect(homehtmlpage)
def savecustomer(request):
    if request.method == "POST":
        Us  = request.POST.get('username')
        pas = request.POST.get('password')
        Em  = request.POST.get('email')
        Cp  = request.POST.get("confirmpassword")
        if pas==Cp:
            obj = deatilescustomer(Username=Us,Password=pas,confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request,"registered successfully")
        return redirect(webloginpage)
def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if deatilescustomer.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request,"login successfully")
            return redirect(homehtmlpage)
        else:
            messages.error(request,"invalid user")
    return render(request,'weblogin.html')
def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully")
    return redirect(webloginpage)
def docloginpage(req):
    return render(req,"doctorlogin.html")
def patientlogin(request):
    if request.method=='POST':
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')

        if doctor.objects.filter(username=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            messages.success(request,"login successfully")
            return redirect(viewbookingfront)
        else:
            messages.error(request,"invalid user")
            return render(request,'doctorlogin.html')
def logoutpatient(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully")
    return redirect(docloginpage)
def bookingpage(request):
    data = appointmentdb.objects.all()
    return render(request, "booking deatiles.html",{'data': data})
def viewbookingfront(req2):
    data = appointmentdb.objects.all()
    return render(req2,"viewbooking_front.html",{'data':data})
