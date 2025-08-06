"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static  
from django.conf import settings  
from Security.views import public_login,public_logintoken,public_view,public_logout
from SystemModule.views import UIConfigs_view,UIConfigDetails_view,UIModule_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', public_login, name='home'),
    path('login/', public_login, name='home'),
    path('logout/', public_logout, name='home'),
    path('home/', public_view, name='home'),
    path('Commons/', public_logintoken, name='home'),
    path('ModuleConfig/', UIConfigs_view, name='Module Configurations'),
    path('ModuleConfig/<str>/', UIConfigDetails_view, name='loginuser'),

    path('module/<str>/', UIModule_view, name='loginuser'),

    path('module/<str>/login/', public_login, name='loginuser'),

    
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

admin.site.site_header = "Plutus Admin"
admin.site.site_title = "Plutus Super Admin Portal"
admin.site.index_title = "Welcome to Plutus Core"