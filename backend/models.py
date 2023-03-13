from django.db import models

# Create your models here.
class admin(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Contactnumber = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="profile",null=True,blank=True)
class department(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Discription=models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
class doctor(models.Model):
    price = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Desc = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Department = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
class contactusdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.EmailField(null=True, blank=True)
    SUBJECT = models.CharField(max_length=100, blank=True, null=True)
    MESSAGE = models.CharField(max_length=500, null=True, blank=True)
class appointmentdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Phonenumber = models.CharField(max_length=100,null=True,blank=True)
    Emailadress = models.CharField(max_length=100,null=True,blank=True)
    Departmentdb= models.CharField(max_length=100,null=True,blank=True)
    Time= models.TimeField(max_length=500, null=True, blank=True)
    Date= models.DateField(max_length=500, null=True, blank=True)
