from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('msgRecv', views.msgRecv, name='msgRecv'),
    path('token', views.token, name='token'),
]