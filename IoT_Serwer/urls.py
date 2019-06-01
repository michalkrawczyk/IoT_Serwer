from django.urls import path
from . import views

app_name = "IoT"

urlpatterns = [
    path('devices', views.DeviceIndexView.as_view(), name='DeviceIndex'),
    # path('colors', views.ColorIndexView.as_view(), name='ColorIndex'),
    # path('color=<int:color_id>',views.ColorDetailView.as_view(), name='ColorDetail'),
    path('device_<pk>/', views.DeviceDetailView.as_view(), name='DeviceDetail'),
    path('error/device=<int:device>', views.ErrorLog.as_view(), name='ErrorLog'),
    # path('sensor/device=<int:device_id>', views.SensorLog.as_view(), name='Sensor'),

]