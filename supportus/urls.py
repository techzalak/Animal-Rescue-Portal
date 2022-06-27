from django.urls import path
from . import views

urlpatterns = [
    path('', views.support),
    path('donate/', views.donate),
    path('payment/',views.pay.as_view(), name='pay'),
    path('payment/charge/',views.charge, name='charge')


    
]