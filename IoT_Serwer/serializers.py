from rest_framework import serializers

from .models import Color, Sensor, CurrentStateData


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('name', 'red', 'blue', 'green')


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('deviceID', 'measure', 'error_flag')


class CurrentStateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentStateData
        fields = (
            'id', 'weather_reading_date_utc', 'red', 'green', 'blue', 'temperature', 'cloudiness', 'shutterPosition',
            'manualControl')
