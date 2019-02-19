from django.urls import path

from . import views

urlpatterns = [
    path('b', views.index, name='index'),
    path('copy', views.copyTableAtoB, name='copyTableAtoB'),
]
