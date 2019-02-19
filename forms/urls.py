from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('printB', views.printB, name='printB'),
    path('copyA', views.copyTableAtoB, name='copyTableAtoB'),
    path('copyButton', views.copyButton, name='copyButton'),
    path('addA', views.addA, name='addA'),
    path('processFormA', views.processFormA, name='processFormA'),
]
