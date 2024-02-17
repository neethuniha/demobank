from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    def __str__(self):
        return self.username

class Branchs(models.Model):
    DIS_CHOICES=[
        ('Idukki','Idukki'),
        ('Eranakulam','Ernakulam'),
        ('Thrissur','Thrissur'),
        ('Kottayam','Kottayam'),
        ('Kozhikode','Kozhikode')
    ]
    branch=models.CharField(max_length=250)
    district=models.CharField(max_length=250,choices=DIS_CHOICES)

    def __str__(self):
        return self.branch

class User1(models.Model):
    GENDER_CHOICES=[
        ('F', 'Female'),
        ('M', 'Male'),
        ('O','Other'),
    ]
    AC_CHOICES = [
        ('S', 'Savings Account'),
        ('C', 'Current Account')
    ]

    username=models.CharField(max_length=250)
    first_name=models.CharField(max_length=250,null=True)
    last_name = models.CharField(max_length=250,null=True)
    dob = models.DateField(null=True)
    phnno = models.IntegerField(null=True)
    email = models.CharField(max_length=250,null=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    address = models.CharField(max_length=250,null=True)
    district=models.CharField(max_length=250,null=True)
    branch = models.CharField(max_length=250,null=True)
    ac_type = models.CharField(max_length=1, choices=AC_CHOICES)
    materials = models.CharField(max_length=200)

    def __str__(self):
        return self.username

