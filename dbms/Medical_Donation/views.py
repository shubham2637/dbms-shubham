from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Collector, Doner


def index(request):
    context= {

    }
    return render(request,"Medical_Donation/index.html",context)

def collectors(request):
    context = {
    "collectors": Collector.objects.all()
    }

    return render(request, "Medical_Donation/collector.html",context)

def collector_add(request):
    context = {
    "collectors": Collector.objects.all()
    }

    return render(request, "Medical_Donation/add-collector.html",context)


def create(request):
    if request.POST:
        coll = Collector(name = request.POST['name'], address = request.POST['address'], pinCode = request.POST['pincode'], Phone_no = request.POST['phone_no'], BirthDate = request.POST['birthdate'], UID = request.POST['BirthDate'], email= request.POST['email'],username = request.POST['username'], password = request.POST['password'], image =request.POST['image'] )
        coll.save()
    return HttpResponseRedirect(reverse("Add_Collector"))
