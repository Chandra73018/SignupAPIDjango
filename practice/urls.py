
from django.contrib import admin
from django.urls import path,include 
from rest_framework import routers
from learn.views import RegisterViewSet




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('learn.urls')),
]
