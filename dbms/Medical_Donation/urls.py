from django.urls import path
from . import views
urlpatterns =[
path("", views.index, name="index"),
path("collector", views.collectors, name= "Collector_view"),
path("add-collector", views.collector_add, name="Add_Collector")

]
