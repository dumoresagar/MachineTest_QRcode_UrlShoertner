
from django.urls import path
from .import views

urlpatterns = [
    path('url/',views.createUrl),
    path('<slug:key>/',views.newurl),
    path('qr/', views.home_view, name='qrcode'),

]
