from django.contrib import admin
from .models import Device, Color
from .models import ErrorData , Sensor

admin.site.register(Device)
admin.site.register(Color)
# admin.site.register(ErrorData)
# admin.site.register(Sensor)

# Zakomentowane tylko sluza tylko do testow
