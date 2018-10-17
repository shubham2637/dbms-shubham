from django.db import models
import os

# Create your models here.

class Doner(models.Model):
    #to store a Image file

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField()
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    image = models.FileField(upload_to='photos/doner')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")



class Collector(models.Model):
    #to store a Image file

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField()
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=16)
    image = models.FileField(upload_to='photos/collector')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")


class Acceptor(models.Model):
    #to store a Image file


    name = models.CharField(max_length=64)
    proprietor = models.CharField(max_length=64)
    license_no = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pincode = models.PositiveIntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=16)
    Phone_no = models.IntegerField()
    image = models.FileField(upload_to='photos/acceptor')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")
