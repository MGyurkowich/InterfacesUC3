from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('perfil/', views.profile, name='web-profile'),
    path('mensajes/', views.messages, name='web-msg')
]
