from rest_framework import serializers
from .models import Color, Sensor


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('name', 'red', 'blue', 'green')


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('deviceID', 'measure', 'error_flag')

