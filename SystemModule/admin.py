from django.contrib import admin

# Register your models here.
from .models import MainModule,ModuleRight,SystemControl
admin.site.register(MainModule)
admin.site.register(ModuleRight)
admin.site.register(SystemControl)

