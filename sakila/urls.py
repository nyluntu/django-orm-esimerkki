from django.urls import path

from . import views

urlpatterns = [
    path('omasivu', views.index, name='index'),
    path('laskesumma', views.laske_summa, name='laske_summa'),
]