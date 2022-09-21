from . import views
from django.urls import path,include
from django.conf import settings
from user import views as user_views
from django.conf.urls.static import static
from driver import urls
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns =[
    path('', views.index_user,name='Home'),
    path('register/', user_views.register, name='register'),
    path('bus/booking/', views.Booking.as_view()),
    # path('access/token/', views.getAccessToken, name='get_mpesa_access_token'),
    # path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('api/buslist/',views.BusList.as_view()),
    path('api/bus/<id>',views.BusDetails.as_view()),
    path('api-token-auth/', obtain_auth_token)
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)