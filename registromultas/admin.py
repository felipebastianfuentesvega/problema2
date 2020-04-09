from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Inspectores, MultasEstacionamiento

admin.site.register(Inspectores)
admin.site.register(MultasEstacionamiento)