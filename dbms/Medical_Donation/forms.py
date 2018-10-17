from django import forms
from .models import *

class Collector_form(forms.ModelForm):
    class Meta:
        model = Collector
        fields = "__all__"
