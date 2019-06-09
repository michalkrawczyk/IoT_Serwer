from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Device, Sensor, ErrorData, CurrentStateData

from .models import Color
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ColorSerializer, SensorSerializer, CurrentStateDataSerializer


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


class ColorList(APIView):
    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class ColorDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Color, pk=pk)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ColorSerializer(snippet)
        return Response(serializer.data)


# SensorList?

class SensorDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Sensor, pk=pk)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ColorSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SensorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentDataDetails(APIView):
    def get(self, request):
        state_data = get_object_or_404(CurrentStateData, pk=1)
        serializer = CurrentStateDataSerializer(state_data)
        return Response(serializer.data)

    def post(self, request):
        state_data = get_object_or_404(CurrentStateData, pk=1)
        serializer = CurrentStateDataSerializer(state_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
