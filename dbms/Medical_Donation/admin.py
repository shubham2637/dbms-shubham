from django.contrib import admin
from .models import Collector, Doner, Acceptor
# Register your models here.

admin.site.register(Doner)
admin.site.register(Collector)
admin.site.register(Acceptor)
