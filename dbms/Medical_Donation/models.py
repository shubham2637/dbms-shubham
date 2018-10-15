from django.db import models
import os


#to store a Image file
#def get_image_path(instance, filename):
#    return os.path.join('photos', str(instance.id), filename)


# Create your models here.

class Doner(models.Model):
    #to store a Image file
    def get_image_path(instance, filename):
        return os.path.join('photos', str(instance.id), filename)


    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField(auto_now=False)
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=16)
    image = models.ImageField(upload_to=get_image_path, blank =True, null=True)


    def __str__ (self):
        return (f"{self.name} {self.address} {self.username} ")

class Collector(models.Model):
    #to store a Image file
    def get_image_path(instance, filename):
        return os.path.join('photos', str(instance.id), filename)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField(auto_now=False)
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=16)
    image = models.ImageField(upload_to=get_image_path, blank =True, null=True)


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")


    class Medical(models.Model):
        #to store a Image file
        def get_image_path(instance, filename):
            return os.path.join('photos', str(instance.id), filename)

        name = models.CharField(max_length=64)
        proprietor = models.CharField(max_length=64)
        license_no = models.CharField(max_length=64)
        address = models.CharField(max_length=128)
        pincode = models.PositiveIntegerField(max_length=6)
        email = models.EmailField()
        username = models.CharField(max_length=64, unique=True)
        password = models.CharField(max_length=16)
        Phone_no = models.IntegerField(max_length=10)
        image = models.ImageField(upload_to=get_image_path, blank =True, null=True)


        def __str__(self):
            return (f"{self.name} {self.username} {self.Phone_no}")
