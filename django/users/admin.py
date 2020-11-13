"""
    Se registra la clase de UseProfiler en el panel de administracion
"""
from users.models import UserProfile
from django.contrib import admin

admin.site.register(UserProfile)


