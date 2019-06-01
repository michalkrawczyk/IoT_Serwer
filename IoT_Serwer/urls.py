from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "IoT"

urlpatterns = [
    path('devices', views.DeviceIndexView.as_view(), name='DeviceIndex'),
    path('colors', views.ColorList.as_view(), name='ColorIndex'),
    path('color=<pk>',views.ColorDetail.as_view(), name='ColorDetail'),
    path('device=<pk>/', views.DeviceDetailView.as_view(), name='DeviceDetail'),
    path('error/device=<int:device>', views.ErrorLog.as_view(), name='ErrorLog'),
    path('sensor=<pk>', views.SensorDetail.as_view(), name='SensorDetail'),
    # path('sensor/device=<int:device_id>', views.SensorLog.as_view(), name='Sensor'),

]
urlpatterns = format_suffix_patterns(urlpatterns)

