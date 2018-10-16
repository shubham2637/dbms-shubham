from .Model import *
import random
import faker


def add_donor():
    d =Doner.objects.get_or_create(pk = random.Random)[0]
    d.save()


def populate(N =5):
    Doner =add_donor()
    
