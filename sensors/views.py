from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Temper, Pressure, HeartBeat, Glucose

# Create your views here.

@csrf_exempt
def get_temper(request, pk):
    temp = Temper(value=pk)
    temp.save()
    return HttpResponse(temp.value)

@csrf_exempt
def temper(request):
    """
    List all code snippets, or create a new snippet.
    """
    temps = Temper.objects.all()
    context = {'title':'Temperature', 'values':temps}
    return render(request, 'sensors/view.html', context)


@csrf_exempt
def get_press(request, pk):
    press = Pressure(value=pk)
    press.save()
    return HttpResponse(press.value)

@csrf_exempt
def press(request):
    """
    List all code snippets, or create a new snippet.
    """
    press = Pressure.objects.all()
    context = {'title':'Pressure', 'values':press}
    return render(request, 'sensors/view.html', context)


@csrf_exempt
def get_heart(request, pk):
    heart = HeartBeat(value=pk)
    heart.save()
    return HttpResponse(heart.value)

@csrf_exempt
def heart(request):
    """
    List all code snippets, or create a new snippet.
    """
    heart = HeartBeat.objects.all()
    context = {'title':'Heart Beat', 'values':heart}
    return render(request, 'sensors/view.html', context)


@csrf_exempt
def get_glucos(request, pk):
    glucos = Glucose(value=pk)
    glucos.save()
    return HttpResponse(glucos.value)

@csrf_exempt
def glucos(request):
    """
    List all code snippets, or create a new snippet.
    """
    glucos = Glucose.objects.all()
    context = {'title':'Glucose', 'values':glucos}
    return render(request, 'sensors/view.html', context)


@csrf_exempt
def all(request):
    """
    List all code snippets, or create a new snippet.
    """
    glucos = Glucose.objects.all()
    heart = HeartBeat.objects.all()
    press = Pressure.objects.all()
    temps = Temper.objects.all()
    context = {'title':'All Measurements', 'glucos':glucos, 'heart':heart, 'press':press, 'temps':temps}
    return render(request, 'sensors/all_sensors.html', context)
