from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('farmers/',include('django.contrib.auth.urls')),
    path('farmers/',include('farmers.urls')),
]
