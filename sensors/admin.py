from django.contrib import admin
from .models import Temper, Pressure, HeartBeat, Glucose
# Register your models here.
admin.site.register(Temper)
admin.site.register(Pressure)
admin.site.register(HeartBeat)
admin.site.register(Glucose)