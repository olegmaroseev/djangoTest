from django.urls import path

from . import views

urlpatterns = [
    path('printB', views.printB, name='printB'),
    path('copyA', views.copyTableAtoB, name='copyTableAtoB'),
    path('copyButton', views.copyButton, name='copyButton'),
]
