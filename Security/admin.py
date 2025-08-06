from django.contrib import admin

# Register your models here.
from .models import Endpoint,SystemUser,SecurityRole,UserRole
admin.site.register(Endpoint)
admin.site.register(SystemUser)
admin.site.register(SecurityRole)
admin.site.register(UserRole)