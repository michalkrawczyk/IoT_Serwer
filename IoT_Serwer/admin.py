from django.contrib import admin
from .models import Device, Color, CurrentStateData, ErrorData, Sensor

admin.site.register(Device)
admin.site.register(Color)
admin.site.register(ErrorData)
admin.site.register(Sensor)
admin.site.register(CurrentStateData)

# Zakomentowane tylko sluza tylko do testow
# Dawaj wszystkie, potem sobie można usunac
