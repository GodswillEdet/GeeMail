from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_email, name='home'),
    path('sent/', views.sent_email, name='sent')
]
