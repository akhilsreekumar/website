from django.shortcuts import render
from .api.serializer import TemperSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Temper

# Create your views here.

@csrf_exempt
def sensors_get(request, pk):
    if request.method == 'GET':
        temp = Temper(value=pk)
        temp.save()
        return HttpResponse(temp.value)
