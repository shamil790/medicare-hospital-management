from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from backend.models import admin, department, doctor, contactusdb, appointmentdb


def indexhtmlpage(request):
    return render(request,"index.html")
def adminpg(req):
    return render(req,"addadmin.html")
def saveadmin(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        Img = request.FILES['image']
        obj = admin(Name=na,Contactnumber=Con,password=pas,Email=Em,username=Us,Image=Img)
        obj.save()
        return redirect(adminpg)
def displayadmin(req2):
    data = admin.objects.all()
    return render(req2,"diplayadmin.html",{'data':data})
def editadmin(req,dataid):
    data = admin.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html", {'data':data})
def Deleteadmin(req, dataid):
    data = admin.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)
def updateadmin(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = admin.objects.get(id=dataid).Image
        admin.objects.filter(id=dataid).update(Name=na,Contactnumber=Con,password=pas,Email=Em,username=Us,Image=file)
        return redirect(displayadmin)
def adddepartment(req):
    return render(req, "adddepartment.html")
def displaydepartment(req2):
    data = department.objects.all()
    return render(req2,"diplaydepartment.html",{'data':data})
def editdepartment(req,dataid):
    data = department.objects.get(id=dataid)
    print(data)
    return render(req,"editdepartment.html", {'data':data})
def Deletedepartment(req, dataid):
    data = department.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydepartment)
def savedepartment(request):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('discription')
        Img = request.FILES['image']
        obj = department(Name=na,Discription=des, Image=Img)
        obj.save()
        return redirect(adddepartment)
def updatedepartment(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        des = request.POST.get('discription')

        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = department.objects.get(id=dataid).Image
        department.objects.filter(id=dataid).update(Name=na,Discription=des, Image=file)
       # data = department.objects.all()
        return redirect(displaydepartment)
def adddoctor(req):
    data =department.objects.all()
    return render(req, "adddoctors.html",{'data':data})
def savedoctor(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        pr = request.POST.get('price')
        Img = request.FILES['image']
        dep = request.POST.get('depart')
        Us = request.POST.get('username')
        pas = request.POST.get('password')
        obj = doctor(Name=na,Desc=de,price=pr,Department=dep,username=Us,password=pas,Image=Img)
        obj.save()
        return redirect(adddoctor)
def displaydoctor(request):
    data = doctor.objects.all()
    return render(request,"displaydoctor.html",{'data':data})
def editdoctor(req,dataid):
    data = doctor.objects.get(id=dataid)
    da = department.objects.all()
    print(data)
    return render(req,"editdoctor.html", {'data':data, 'da':da})
def Deletedoctor(req, dataid):
    data = doctor.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydoctor)
def updatedoctor(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        pr = request.POST.get('price')
        dep = request.POST.get('depart')
        Us = request.POST.get('username')
        pas = request.POST.get('password')

        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = doctor.objects.get(id=dataid).Image
        doctor.objects.filter(id=dataid).update(Name=na,Desc=de,price=pr,Department=dep,username=Us,password=pas,Image=file)
        # data = category.objects.all()
        return redirect(displaydoctor)
def loginpage(request):
    return render(request,"login.html")
def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password'] = password_r
                return redirect(indexhtmlpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def displaymsg(request):
    data = contactusdb.objects.all()
    return render(request, "contactme.html", {'data': data})
def Deletemsg(req, dataid):
    data = contactusdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymsg)
def displaybook(request):
    data =appointmentdb.objects.all()
    return render(request, "Booking.html", {'data': data})
def Deletebook(req, dataid):
    data = appointmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaybook)





