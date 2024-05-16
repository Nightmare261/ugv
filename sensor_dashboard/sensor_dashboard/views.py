# sensor_dashboard/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData, UGVPosition

def get_sensor_data(request):
    sensor_data = SensorData.objects.all().order_by('-timestamp')[:10]  # Example: Fetch last 10 records
    data = {'sensor_data': list(sensor_data.values())}
    return JsonResponse(data)

def get_ugv_position(request):
    ugv_position = UGVPosition.objects.latest('timestamp')
    data = {
        'x': ugv_position.x,
        'y': ugv_position.y,
        'z': ugv_position.z,
        'speed': ugv_position.speed
    }
    return JsonResponse(data)
