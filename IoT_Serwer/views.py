from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Device, Sensor, ErrorData

from .models import Color


class DeviceIndexView(generic.ListView):
    template_name = 'server/deviceIndex.html'
    context_object_name = 'allDevices'

    def get_queryset(self):
        return Device.objects.all()


class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = 'server/deviceDetail.html'


class ErrorLog(generic.ListView):
    template_name = 'server/errorLog.html'
    context_object_name = 'errorList'

    def get_queryset(self):
            dev = get_object_or_404(Device, pk=self.kwargs['device'])
            return ErrorData.objects.filter(deviceID=dev.pk)

    def get_context_data(self, **kwargs):
        dev = get_object_or_404(Device, pk=self.kwargs['device'])
        context = super().get_context_data(**kwargs)
        context['dev'] = dev
        return context
#
#
# class SensorLog(generic.DetailView):
#     model = Sensor
#     template_name = 'server/sensorLog.html'








''' Robic tez CreateView? '''

