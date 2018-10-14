from django.shortcuts import render
from django.http import HttpResponse, Http404
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
