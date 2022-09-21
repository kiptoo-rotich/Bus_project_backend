from . import views
from django.urls import path,include
from django.conf import settings

urlpatterns =[
    path('drivers/', views.index_admin,name='drivers'),
    path('admin_dashboard/', views.dash_admin,name='Admindash'),
    path('Edit_bus/<id>', views.editbus,name='editbus'),
    path('Edit_user/<id>', views.edituser,name='edituser'),
    path('Delete_bus/<id>', views.deletebus,name='deletebus'),
    path('Delete_user/<id>', views.deleteuser,name='deleteuser'),
    path('Delete_driver/<id>', views.deletedriver,name='deletedriver'),
    path('Edit_driver/<id>', views.editdriver,name='editdriver'),
    path('Buses/', views.buses,name='buses'),
    path('Users/', views.users,name='users'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
    ]