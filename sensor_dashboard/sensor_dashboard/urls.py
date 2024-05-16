# sensor_dashboard/urls.py

from django.urls import path
from .views import get_sensor_data, get_ugv_position

urlpatterns = [
    path('api/sensor-data/', get_sensor_data, name='sensor_data_api'),
    path('api/ugv-position/', get_ugv_position, name='ugv_position_api'),
]
