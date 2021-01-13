from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('perfil/', views.profile, name='web-profile'),
    path('mensajes/', views.messages, name='web-msg'),
    path('facturas/', views.bills, name='web-bills'),
    path('monedero/', views.payments, name='web-pm'),
    path('calendario/', views.calendar, name='web-cal'),
    path('ajustes/', views.ajustes, name='web-aju'),
    path('nuevo_metodo_pago/', views.new_met_pago, name='web-np')
]
