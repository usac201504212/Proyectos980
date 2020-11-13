"""
    venta_ropa URL Configuration
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from venta_ropa import views as general
from users import views as users

urlpatterns = [
    path('', general.homepage, name = "homepage"),
    path('admin/', admin.site.urls, name = "administration"),
    path('login/', users.logon, name = "logon"),
    path('logout/', users.logout_view, name = "logout"),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT) 

