from django.shortcuts import render
from .api.serializer import TemperSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Temper

# Create your views here.

@csrf_exempt
def sensors_get(request, pk):
    if request.method == 'GET':
        temp = Temper(value=pk)
        temp.save()
        return HttpResponse(temp.value)

@csrf_exempt
def sensors(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temps = Temper.objects.all()
        serializer = TemperSerializer(temps, many=True)
        return JsonResponse(serializer.data, safe=False)