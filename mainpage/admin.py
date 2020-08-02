from django.contrib import admin

# Register your models here.

from .models import Aporte
from .models import Empleado
from .models import Empresa
from .models import Trabajo

admin.site.register(Aporte)
admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Trabajo)