from enum import Enum

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ShutterState(Enum):
    DOWN = 1
    UP = 0
    ERROR = 2


class CustomModels:

    @staticmethod
    def color_field():
        return models.IntegerField(
            default=0,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(255)
            ]
        )

    @staticmethod
    def temperature_field():
        return models.IntegerField(
            default=20,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(100)
            ]
        )

    @staticmethod
    def shutter_state():
        return models.IntegerField(
            default=2,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(2)
            ]
        )


class Device(models.Model):
    group = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(31)
        ]
    )
    name = models.TextField(max_length=100)

    def __str__(self):
        return str(self.id) + " - " + self.name


class Sensor(models.Model):
    deviceID = models.ForeignKey(Device, on_delete=models.CASCADE)
    date = models.DateTimeField()
    measure = models.FloatField()
    error_flag = models.BooleanField()

    def __str__(self):
        return str(self.date) + " , ID:" + str(self.deviceID) + ", Measure:" + str(self.measure)


class ErrorData(models.Model):
    deviceID = models.ForeignKey(Device, on_delete=models.CASCADE)
    date = models.DateTimeField()

    # lastCommand = models.TextField()?

    def __str__(self):
        return str(self.date) + " , ID:" + str(self.deviceID)


class Color(models.Model):
    name = models.CharField(max_length=100)
    red = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(255)
        ]
    )
    blue = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(255)
        ]
    )
    green = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(255)
        ]
    )

    def __str__(self):
        return str(self.name)


class CurrentStateData(models.Model):
    red = CustomModels.color_field()
    green = CustomModels.color_field()
    blue = CustomModels.color_field()
    temperature = CustomModels.temperature_field()
    shutterState = CustomModels.shutter_state()
    manualControl = models.BooleanField(default=False)
