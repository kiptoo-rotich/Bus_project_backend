from . import views
from django.urls import path,include
from django.conf import settings

urlpatterns =[
    path('', views.index_driver,name='Home'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
    ]